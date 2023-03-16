import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint


try:
    # Set up the Chrome driver
    service = Service('/opt/homebrew/bin/chromedriver')
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # run Chrome in headless mode (without opening a window)
    driver = webdriver.Chrome(service=service, options=options)

    # Load the webpage
    driver.get('https://www.investing.com/funds/amundi-msci-wrld-ae-c-historical-data')

    # Select the date picker element and change the date range to 2020
    date_picker = driver.find_element(By.ID,"widgetField")

    """startDate = driver.find_element(By.ID,'startDate')
    endDate = driver.find_element(By.ID,'endDate')
    applyBtn = driver.find_element(By.ID,'applyBtn')"""
    XPATH = '/html/body/div[7]/div[1]/input[1]'

    #test = driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/input[1]')
    print(XPATH)
    
    #date_picker = driver.find_element(By.ID,"flatDatePickerCanvasHol)
    #date = date_picker.getAttribute("value")
    #date_picker = Select(WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, 'widgetFieldDateRange'))))
    """print(date_picker.text)
    print(startDate.text)
    print(endDate.text)
    print(applyBtn.text)"""
    #print(test)
    #print(test.text)

except Exception as e:
    print(e)
    traceback.print_exc()
    input("press any key to end")