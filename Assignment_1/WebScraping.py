# Using Selenium library for web scraping and csv module for converting to CSV file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# XPATH's for elements in web page
DATE_XPATH =  "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span"
START_XPATH = "//*[@id=\"startDate\"]"
END_XPATH = "//*[@id=\"endDate\"]"
START_DATE = "01/01/2020"
END_DATE = "12/31/2020" 
APPLY_XPATH =  "//*[@id=\"applyBtn\"]"
HEADER_XPATH = "//*[@id=\"curr_table\"]/thead/tr"
BODY_XPATH = "//*[@id=\"curr_table\"]/tbody"

# Scrape table data in specified date range from browser
def getTableData (wd):
    date_picker = WebDriverWait(wd,30).until(EC.element_to_be_clickable((By.XPATH,DATE_XPATH)))
    wd.execute_script("arguments[0].click();", date_picker)
        
    start_date = wd.find_element(By.XPATH,START_XPATH)
    start_date.clear()
    start_date.send_keys(START_DATE)
    end_date = wd.find_element(By.XPATH,END_XPATH)
    end_date.clear()
    end_date.send_keys(END_DATE)
    apply_button = wd.find_element(By.XPATH,APPLY_XPATH)
    wd.execute_script("arguments[0].click();", apply_button)
    table_data_header = WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.XPATH, HEADER_XPATH)))
    table_data_body = WebDriverWait(wd, 30).until(EC.presence_of_element_located((By.XPATH, BODY_XPATH)))
    
    return [table_data_header, table_data_body]

# Convert to CSV file
def convertToCSV(headerList, bodyList):
    headerList = str.split(headerList.text)
    headerList[-2:] = [' '.join(headerList[-2:])]
    rows = bodyList.text.strip().split('\n')
    data = [row.split() for row in rows]
    data_combined = [[sublist[0] + ' ' + sublist[1] + ' ' + sublist[2]] + sublist[3:] for sublist in data]
    
    with open('amundi-msci-wrld-ae-c.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(headerList)
        write.writerows(data_combined)

# Main function
def main():
    try:
        wd = webdriver.Chrome()
        wd.get('https://www.investing.com/funds/amundi-msci-wrld-ae-c-historical-data')
        wd.maximize_window()
        wd.execute_script("window.scrollTo(0,300)")
        tableData = getTableData(wd)
        convertToCSV(tableData[0], tableData[1])
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        wd.quit()
        
# Initialize main function
if __name__ == "__main__":
    main()