from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

assets = ("Amundi Index Msci World Ae-c",
        "iShares Global Corporate Bond UCITS (CRPS)",
        "Xtrackers II Global Government Bond UCITS ETF 5C (XG7S) ETF",
        "SPDR® Gold Shares (GLD) ETF",
        "US Dollar Index (DXY)"
       )

links= ("https://www.investing.com/funds/amundi-msci-wrld-ae-c-historical-data",
        "https://www.investing.com/etfs/ishares-global-corporate-bond-$-historical-data",
        "https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5-historical-data",
        "https://www.investing.com/etfs/spdr-gold-trust-historical-data",
        "https://www.investing.com/indices/usdollar-historical-data"
        )

fileNames = ("amundi-msci-wrld-ae-c.csv",
            "ishares-global-corporate-bond-$.csv",
            "db-x-trackers-ii-global-sovereign-5.csv",
            "spdr-gold-trust.csv",
            "usdollar.csv")
i = 0
for asset in assets:
    name = asset
    link = links[i]
    fileName = fileNames[i]

    if (name == "Amundi Index Msci World Ae-c"):
        date_xpath =  "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span"
        start_xpath =  "//*[@id=\"startDate\"]"
        end_xpath = "//*[@id=\"endDate\"]"
        startDate = "01/01/2020"
        endDate = "12/31/2020" 
        apply_xpath =  "//*[@id=\"applyBtn\"]"
        table_xpath = "//*[@id=\"results_box\"]"
    else:
        date_xpath = "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div/div[1]"
        start_path = "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input"
        #             "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input"
        end_path = "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input"
        startDate = "2020-01-01"
        endDate = "2020-12-31"
        apply_xpath = "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button"
        table_xpath = "//*[@id=\"__next\"]/div[2]/div/div/div[2]/main/div/div[5]/div/div/div[3]/div/table"

    print(name)
    print(link)
    print(fileName)
    #open WebDriver
    wd = webdriver.Chrome()
    #insert link per asset
    wd.get(link)

    #open window and maximize it
    print(wd.get_window_size())
    wd.maximize_window()
    print(wd.get_window_size())
    wd.execute_script("window.scrollTo(0,400)")

    # Select the date picker element and change the date range to 2020
    #print(wd.find_element(By.XPATH,date_xpath))
    date_picker = WebDriverWait(wd,30).until(EC.element_to_be_clickable((By.XPATH,date_xpath)))

    # Click on the element using JavaScript
    wd.execute_script("arguments[0].click();", date_picker)

    # Clear the fields and fill with the date content   
    start_date = WebDriverWait(wd,30).until(EC.element_to_be_clickable((By.XPATH,start_xpath)))
    start_date.clear()
    start_date.send_keys(startDate)
    end_date = WebDriverWait(wd,30).until(EC.element_to_be_clickable((By.XPATH,end_xpath)))
    end_date.clear()
    end_date.send_keys(endDate)
    apply_button = wd.find_element(By.XPATH,apply_xpath)
    wd.execute_script("arguments[0].click();", apply_button)

    #get Table data
    table_data = WebDriverWait(wd,30).until(EC.text_to_be_present_in_element_attribute((By.XPATH,table_xpath), "innerHTML" , "High"))
    #print(table_data)

    #transform table data into CSV file and store as CSV
    table = wd.find_element(By.XPATH,table_xpath).get_attribute('innerHTML')
    #print(table)
    table_pd = pd.read_html(table)
    pd_df = table_pd[0]
    pd_df.to_csv(fileName)
    i+=1
    print(i)
    #wd.quit()


    