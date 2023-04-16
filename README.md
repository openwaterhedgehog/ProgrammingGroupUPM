# ProgrammingGroupUPM

# READ ME 

## Description of the content (files and dirs.) 
The project is divided into two folders: assignment 1 and 2
- Assignment 1 handles the web scraping functionality to create the csv files
- The files for data generation and data analysis are in the folder assignment 2.

## Running the project


### Web scraping (assignment 1): 
1. Install Required Packages:

    This code requires the following Python packages to be installed:
        selenium (version 3.141.0 or higher)
        csv (version 1.0 or higher)

    Requires that you have the Chrome browser and the ChromeDriver executable on your system and added it to your system's PATH environment variable, because the script uses ChromeDriver to interact with the Chrome browser.
 
 2. Run the script in terminal where the script is stored:
    python web_scraping.py

### Data generation (assignment 2):
Prerequisite: To execute the code the packages from the *requirements.txt* (in folder Assignment_2) need to be installed.

### Data analysis (assignment 2):
This part is not executable. The results can be found in the pdf document. For a closer look open the analysis.ipynb in a Jupyter Notebook environemnt. The cells should be executed sequentially.


## Modules
| Part  | Module  | Description  |   
|---|---|---|
| Assignment 1  | **Webscraping.py**   | Opens the Chrome browser, gets table data based on a specified date range, collects table data, converts into CSV file, stores CSV file. Uses Selenium library and CSV module. Defines two functions - 'getTableData()' and 'convertToCSV()' to perform the web scraping and the conversion to CSV.  |  
| Assignment 2 | **XX.py**   | XXX  |  
| Assignment 2 | **analysis.ipynb**   | Juypter notebook handling the data analysis.  | 
| Assignment 2 | **2.1 Data Analysis Report.pdf**   | Final data analysis report containing the conclusions of our investment strategies analysis.  |   




