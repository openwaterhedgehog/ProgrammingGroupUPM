# ProgrammingGroupUPM

# READ ME 

## Description of the content (files and dirs.) 
There are two folders, assignment 1 and 2. Web scraping to csv file is in folder assignment 1, while the files for data generation and data analysis is in folder assignment 2.

## Running the project

Web scraping (assignment 1): 
1. Install Required Packages:

This code requires the following Python packages to be installed:
selenium (version 3.141.0 or higher)
csv (version 1.0 or higher)

Requires that you have the Chrome browser and the ChromeDriver executable on your system and added it to your system's PATH environment variable, because the script uses ChromeDriver to interact with the Chrome browser.
 
 2. Run the script in terminal where the script is stored:
python web_scraping.py

Data generation (assignment 2):

Data analyis (assignment 2):

## Modules

Web scraping (assingment 1):
Webscraping.py
Description: open Chrome browser, gets table data based on specified date range, collects table data, converts into CSV file, stores CSV file. Uses Selenium library and CSV module. Defines two functions - 'getTableData()' and 'covnertToCSV()' to perform the web scraping and the conversion to CSV.



