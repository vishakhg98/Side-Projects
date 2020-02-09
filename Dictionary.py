"""
pip install beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup


def replay():
    return input("\nEnter 'y' to Search Again! : \n\n").lower().startswith('y')

while True:
    try:
        word = input("Enter the word : ")

        data = requests.get("https://en.oxforddictionaries.com/definition/" + word)
        soup = BeautifulSoup(data.text, "html.parser")

        #<meta name="description" content="Cold definition, having a relatively low temperature; having little or no warmth: cold water; a cold day. See more.">

        data1 = soup.find('span', {"class": "ind"})
        print(data1.string)
    except:
        print("Error:Word not found.\nPlease check the spelling or try an another word.")
        
    if not replay():
        break
