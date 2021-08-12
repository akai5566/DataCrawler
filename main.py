#Use python3.6
import requests
import time
import random
from bs4 import BeautifulSoup 
import requests.packages.urllib3

#Solve "InsecureRequestWarning: Unverified HTTPS request is being made"
uests.packages.urllib3.disable_warnings() 

#i start from 0 to 274001 with interval = 100 
for i in range (0, 274001, 100): 
	
	#Fill in the url where you want to crawl the data
    url = "https://building.tycg.gov.tw/opendata/OpenDataSearchUrl.do?=100&d=OPENDATA&c=BUILDLIC&Start=%i" 

    #Get the result data from the url 
    r = requests.get(url%i, verify = False)
    
    #Print the result information
    print(i)
    print(url%i)

    #Save the result as json format
    print(r.text, end=' ', file=open(f'file_start_from_{i}.json', 'a'))
    print("============================================= 我是分隔線 =============================================")

    #Set a delay 
    time.sleep(2) 
