# beautifulsoup module is required for this program
# pip install beautifulsoup4


from bs4 import BeautifulSoup
import requests


def replay():
    return input("\n\n\nEnter 'y' to Search Again! : ").lower().startswith('y')

session = requests.Session()
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

while True:
    # user agent and language is used as a loophole to get data from google 
    

    print("\n\n\nPress Enter to search Weather of your current location with help of your IP Address ")
    city = input("\n\nEnter the city : ")
    print("\n\nCalculating Weather....")

    # https://www.google.com/search?q=weather+delhi
    url = "https://www.google.com/search?q=weather+" + city

    html = session.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    temp = soup.find("span", attrs={"id": "wob_tm"}).text
    loc = soup.find("div", attrs={"id": "wob_loc"}).text
    dayhr = soup.find("div", attrs={"id": "wob_dts"}).text
    sky_condition = soup.find("span", attrs={"id": "wob_dc"}).text
    rain = soup.find("span", attrs={"id": "wob_pp"}).text
    humidity = soup.find("span", attrs={"id": "wob_hm"}).text
    wind = soup.find("span", attrs={"id": "wob_ws"}).text
    
    print("\n"*50)
    print("Temperature   : "+ temp+ "%")
    print("Location      :", loc)
    print("Day and Time  :", dayhr)
    print("Description   :", sky_condition)
    print("Precipitation :", rain)
    print("Humidity      :", humidity)
    print("Wind Speed    :", wind)

    if not replay():
        break