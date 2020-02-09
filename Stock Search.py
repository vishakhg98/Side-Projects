"""
pip install beautifulsoup4
"""

import re
import urllib.request

def replay():
    return input("\nEnter 'y' to search again! : ").lower().startswith('y')

while True:
    try:
        #https://in.finance.yahoo.com/quote/   <== add the stock name at the end

        stock = input("\nEnter the stock name : ")

        url = "https://stocktwits.com/symbol/" +stock

        print("Source :",url)

        data = urllib.request.urlopen(url).read()
        data1 = data.decode("utf-8")
        #print(data1)
        # st_3OTz8Ec">  <= after this stock value is given in 'view page source'
        m = re.search("st_3OTz8Ec\">", data1) #st_3OTz8Ec\"> : HERE \ is an escape character
        #print(m)
        start = m.end()
        end = start + 20
        newString = data1[start:end]
        #print(newString)
        m = re.search("/", newString)
        start = 0 #To remove the 'st_3OTz8Ec\">' line and print only the stock value
        end = m.end() - 2
        newString2 = newString[start:end]
        #print(newString2)

        print("\nThe stock value of " + stock.upper() + " is " + str(newString2) +"\n")
    except:
        print("Error: " +stock+ " stock name is incorrect. \n Please enter the correct Stock name.\n")
    
    if not replay():
        break