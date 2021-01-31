# Naukri.com Job Listing Python Scraping
A simple Python script made for a college project to scrape job listings using search keywords from Naukri.com using Selenium, BeautifulSoup and Pandas
### Setup
Run the following commands in the terminal to install the required Python Modules<br>
`pip install beautifulsoup4`<br>
`pip install selenium`
### Config
Edit the following lines in the `naukri.py` file before running it to make sure the correct directories are setup. <br>
If this isn't properly set, Selenium will refuse to initialise and the program will not run. <br>
`driver = webdriver.Chrome(“C:\\Path\To\chromedriver.exe”)`<br>
`df.to_csv("C:\\Path\To\Desktop",index=False)`
<br>
Download the latest Chromium selenium drivers and ensure your Chrome browser is upto date before running the Python script. <br>
Get the latest drivers  <a href=https://chromedriver.chromium.org/downloads>here</a> <br>
