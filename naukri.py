from selenium import webdriver
from bs4 import BeautifulSoup 
import time
import pandas as pd

df = pd.DataFrame(columns=['Title','Company','Location'])

pages = int(input("Enter the number of pages to collect result from: "))

for page in range(1,pages+1):
    url = "https://www.naukri.com/python-jobs" + "-" + str(page)
    #Go to this link to get the latest chrome drivers
    # https://chromedriver.chromium.org/downloads

    #MacOS Selenium Drivers
    #driver = webdriver.Chrome("/Users/abhiklodh/Downloads/chromedriver")
    driver = webdriver.Safari()

    #Windows Selenium Drivers
    #driver = webdriver.Chrome(“C:\\Downloads\chromedriver.exe”)
    
    driver.get(url)

    time.sleep(3)

    soup = BeautifulSoup(driver.page_source,'html5lib')

    #print(soup.prettify())

    driver.close()

    results = soup.find(class_='list')
    job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')

    for job_elem in job_elems:

        #Post Title
        Title = job_elem.find('a',class_='title fw500 ellipsis')

        # Company Name
        Company = job_elem.find('a',class_='subTitle ellipsis fleft')

        #Location for the job post
        Loc = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi location')
        Loc_exp = Loc.find('span',class_='ellipsis fleft fs12 lh16')
        if Loc_exp is None:
            continue
        else:
            Location = Loc_exp.text

        #Appending data to the DataFrame 
        df=df.append({'Title':Title.text,'Company':Company.text,'Location':Location},ignore_index = True)

df.to_csv("/Users/abhiklodh/Downloads/naukri.csv",index=False)
