# ProgrammingGroupUPM - READ ME 

## Description of the content (files and dirs.) 
The project is divided into two folders: assignment 1 and 2
- Assignment 1 handles the web scraping functionality to create the csv files
- The files for data generation and data analysis are in the folder assignment 2.

The portfolio generation works with the generated csv files of the scraped data in assignment 1.

But as the parts were performed in parallel, the portfolio data analysis (part 2.1) is based on the data from moodle and not the scraped data. The porfolio and calculated returns and volatilities are saved in the file *portfolio_metrics_historical_data.csv*. This is the result of running the Evaluation.py script.


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
Prerequisite: To execute the code the packages from the *requirements.txt* (in folder Assignment_2) need to be installed. Taking start date (e.g. 01/01/2020), end date (e.g. 12/31/2020) and csv files to process as arguments. The csv files must have a column with name "Date" in a date format like "Dec 31, 2020" and a column with "Price". The input date formats can be changed in the first lines of the script. We changed the provided csv files from the assignment, so pandas can read them.
    python Evaluation.py 01/01/2020 12/31/2020 Historical_Prices_Csv/*.csv



### Data analysis (assignment 2):
This part is not executable. The results can be found in the pdf document. For a closer look open the analysis.ipynb in a Jupyter Notebook environemnt. The cells should be executed sequentially.


## Modules
| Part  | Module  | Description  |   
|---|---|---|
| Assignment 1  | **Webscraping.py**   | Opens the Chrome browser, gets table data based on a specified date range, collects table data, converts into CSV file, stores CSV file. Uses Selenium library and CSV module. Defines two functions - 'getTableData()' and 'convertToCSV()' to perform the web scraping and the conversion to CSV.  |  
| Assignment 2 | **Evaluation.py**   | Python script processing the csv files and writing results to "result.csv". |  
| Assignment 2 | **analysis.ipynb**   | Juypter notebook handling the data analysis.  | 
| Assignment 2 | **2.1 Data Analysis Report.pdf**   | Final data analysis report containing the conclusions of our investment strategies analysis.  |   