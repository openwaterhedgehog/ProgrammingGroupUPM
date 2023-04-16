#!python

import pandas
import sys
import math
from datetime import datetime

ARG_DATE_FORMAT = '%m/%d/%Y'
FILE_DATE_FORMAT = '%b %d, %Y'

# Calculates
def calculate_combinations(n, m):
    return math.factorial(m + n - 1) / (math.factorial(n) * math.factorial(m - 1))

def combine_help(assets, rest, step):
    if len(assets) == 1:
        asset = assets[0].copy()
        asset["shares"] = abs(round(rest, ndigits=3))
        return [[asset]]

    out = list()
    for x in [i * step for i in range(int((rest / step) + 1.0000001))]:
        combinations = combine_help(assets[1:], rest-x, step)
        for combination in combinations:
            asset = assets[0].copy()
            asset["shares"] = abs(round(x, ndigits=3))
            combination.append(asset)

        out += combinations

    return out


# takes a dict and produces list of combinations of its elements [[{"shares": float}]]
# while adding the respective share to the dict
def combine(assets):
    return combine_help(assets, 1.0, 1.0/len(assets))


# Takes in a dict with "Date" list of format "MM/DD/YYYY" and "Price" list and outputs
# a dictionary with with date in datetime format and prices in one dictionary and
# filtered with respect to the start end end date
def prepare_table(table, date_start, date_end):
    new_table = dict()

    prices = dict()
    #prices_sum = 0
    for row, date in table["Date"].items():
        date = datetime.strptime(table["Date"][row], FILE_DATE_FORMAT)

        if date <= date_end:
            if date < date_start:
                break

            #prices_sum += table["Price"][row]
            prices[date] = table["Price"][row]

    new_table["prices"] = prices
    #avg = prices_sum / len(prices)
    #var = math.sqrt(sum(map(lambda x: (x - avg) ** 2, prices.values())) / len(prices))
    #new_table["volatility"] = (var / avg) * 100

    return new_table


# takes combinations of various assets of the format [[{"name": str, "shares": float, "prices": {datetime: float}}]]
# and output of format [{<<name>: <probability>>, "RETURN": float, "VOLAT": float}] containing the respective
# asset combination, return and volatility
def calculate_return_volatility(combinations):
    ret_dict = {asset["name"]: list() for asset in combinations[0]}
    ret_dict["RETURN"] = list()
    ret_dict["VOLAT"] = list()

    # Calculate for each possible combination
    for combination in combinations:
        for asset in combination:
            ret_dict[asset["name"]].append(asset["shares"])

        # Calculate portfolio return
        buy_amount = sum([asset["prices"][min(asset["prices"].keys())] * asset["shares"] for asset in combination])
        current_value = sum([asset["prices"][max(asset["prices"].keys())] * asset["shares"] for asset in combination])
        portfolio_return = 100 * (current_value - buy_amount) / buy_amount
        ret_dict["RETURN"].append(portfolio_return)

        values = list()

        # Calculate volatility
        for date in combination[0]["prices"].keys():
            if all([date in asset["prices"] for asset in combination[1:]]):
                value_day = sum([asset["prices"][date] * asset["shares"] for asset in combination])
                values.append(value_day)

        avg = sum(values) / len(values)
        var = math.sqrt(sum(map(lambda x: (x - avg) ** 2, values)) / len(values))
        ret_dict["VOLAT"].append((var / avg) * 100)

    return ret_dict
                


if __name__ == '__main__':
    assets = list()
    date_start = datetime.strptime(sys.argv[1], ARG_DATE_FORMAT)
    date_end = datetime.strptime(sys.argv[2], ARG_DATE_FORMAT)

    for i in range(3, len(sys.argv)):
        table = pandas.read_csv(sys.argv[i])
        asset = prepare_table(table.to_dict(), date_start, date_end)
        asset["name"] = sys.argv[i]
        assets.append(asset)

    #assets = [{'ST': 50}, {'CB': 50}, {'PB': 50}, {'GO' : 50},{'CA': 50}]
    asset_combinations = combine(assets)
    #print(asset_combinations, len(asset_combinations))
    result = calculate_return_volatility(asset_combinations)
    #for out in result:
    #    print(out)

    pandas.DataFrame.from_dict(result).to_csv("result.csv")