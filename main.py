import csv                                                                             #Downloads and transcribes json coindesk API data into python
import json
import requests
import time
import datetime
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def bitcoin():                                                                          #Parses through API data and pulls the USD bitcoin price value
    

    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    todos = json.loads(response.text)

    x=todos['bpi']
    y= x['USD']
    z= y['rate_float']

    print(z)
    return z


def numbers(cell_list):
# Can I write a code that checks to see if "Date, Time, BTC Price headers already exist.
# # keep program from printing it again       ---> New Project <---
 
    
    # "a" appends data to file instead of overriding previous data                                                                          
    filename = "bitcoinPrices.csv"
    headers = "Date, Time, BTC Price\n"                                             # initial setup for writing to a csv:
    f = open(filename,"a")                   
    price = bitcoin()                       
    upload = datetime.datetime.now()                                        
    time1 = upload.strftime("%X")                                            
    date = upload.strftime("%x")

    # With _ as _  allows python to open and close specified file when deemed necessary
    with f as file_inserts_data:                                    
        f.write(date + "," + time1 + "," + str(price) + '\n')       # what does write() do?             
        
        if 32_000 > price > 31_900:                                             
            print("Meh")
    
        else:    
            for cell_number in cell_list:                
                path = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(path)
                driver.get("https://www.opentextingonline.com/")

                phone_number = driver.find_element_by_id("phone")
                phone_number.send_keys(cell_number)                                  #Enters number                          
                time.sleep(2)                                                        #Sleep timers are necessary so the code doesn't outpace the website                                     

                text = driver.find_element_by_id("tmessage")                    
                text.send_keys("Bitcoin's price is "+ str(price))
                time.sleep(2)

                send_it = driver.find_element_by_id("btsend")                        #Hits send button        !!!!! BUTTON IS NOT HITTING !!!!!                 
                send_it.send_keys(Keys.RETURN)
                time.sleep(6)

                    
                driver.close()
            
    time.sleep(35.90)                                                                #Sleeps for 1 hour
    f = open(filename,"a")

numbersList= ["5555555555"]
numbers(numbersList)  
