# This file creates and scraes the internet!
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import sqlite3

# COnnect and create databse
connection = sqlite3.connect("creditcard.db")
crsr = connection.cursor()
# MAIN TABLE
table = """CREATE TABLE creditcards(
id INTEGER PRIMARY KEY,
name VARCHAR(20),
credit_low INTEGER,
credit_high INTEGER);
"""
# non main table
benefitTable = """
CREATE TABLE benefits(
id INTEGER PRIMARY KEY,
desc VARCHAR(100),
creditcard FORIGN KEY
)"""
# crsr.execute(table)
# crsr.execute(benefitTable)

# URLs to scrape through
chaseUrl = [
    "https://creditcards.chase.com/cash-back-credit-cards/chase-freedom-unlimited?CELL=6TKX&jp_aid=cc/mptarg1/int/FREU/ccrew1",
    "https://creditcards.chase.com/rewards-credit-cards/chase-sapphire-preferred?CELL=6TKX&jp_aid=cc/mptarg1/int/SAPP/ccrew2",
    "https://creditcards.chase.com/travel-credit-cards/marriott-bonvoy-boundless?CELL=6TKX&jp_aid=cc/mptarg1/int/MARC/cctrav1",
    "https://creditcards.chase.com/cash-back-credit-cards/chase-freedom?CELL=6TKX",
    "https://creditcards.chase.com/rewards-credit-cards/chase-sapphire-reserve?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/southwest-priority?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/southwest-plus?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/southwest-premier?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/united-explorer?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/united-travelbank?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/united-mileageplus-club?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/british-airways?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/aer-lingus?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/marriott-bonvoy-bold?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/world-of-hyatt-credit-card?CELL=6TKX",
    "https://creditcards.chase.com/rewards-credit-cards/disney-premier?CELL=6TKX"
    "https://creditcards.chase.com/rewards-credit-cards/disney-rewards?CELL=6TKX",
    "https://creditcards.chase.com/travel-credit-cards/ihg-rewards-club-premier?CELL=6TKX",
    "https://creditcards.chase.com/rewards-credit-cards/starbucks-rewards?CELL=6TKX",
    "https://creditcards.chase.com/cash-back-credit-cards/amazon-rewards?CELL=6TKX",
    "https://creditcards.chase.com/small-business-credit-cards/ink-unlimited?CELL=6TKX",
    "https://creditcards.chase.com/small-business-credit-cards/ink-cash?CELL=6TKX",
    "https://creditcards.chase.com/small-business-credit-cards/ink-business-preferred?CELL=6TKX"
]

coCard = [
    "https://www.capitalone.com/credit-cards/venture/",
    "https://www.capitalone.com/credit-cards/savor-dining-rewards/",
    "https://www.capitalone.com/credit-cards/savorone-dining-rewards/"
]


def webScrap(urls):
    for data in urls:
        response = requests.get(data)
        page = urlopen(data)
        soup = BeautifulSoup(page, "html.parser")
        if urls == chaseUrl:
            parseChase(soup)
        if urls == coCard:
            parseCoCard(soup)


def parseChase(soup):
    # New arrayeach time
    for element in soup.find_all("sup"):
        element.decompose()
    text = soup.get_text()
    # Grabs the title of the credit cards
    titlebox = soup.find("h1", attrs={'class': "card-title"})
    # benefitsbox = soup.find("div", attrs = {'class', "primary-item"})
    title = titlebox.text.strip()
    print(title)
    # benefits = benefitsbox.text.strip()
    command = """INSERT INTO creditcards(id, name, credit_low, credit_high)
    VALUES (NULL, '{title}', 22, 44);"""
    command = command.format(title=title)
    crsr.execute(command)
    connection.commit()


def parseCoCard(soup):
    text = soup.get_text()
    titlebox = soup.find("h1", attrs={'class': 'non-mobile'})
    title = titlebox.text.strip()
    print(title)
    command = """INSERT INTO creditcards(id, name, credit_low, credit_high)
    VALUES (NULL, '{title}', 22, 44);"""
    command = command.format(title=title)
    crsr.execute(command)
    connection.commit()


def printDb():
    crsr.execute("SELECT * FROM creditcards")
    print("fetchall:")
    result = crsr.fetchall()
    for r in result:
        print(r)


def main():
    # webScrap(chaseUrl)
    webScrap(coCard)
    printDb()
    connection.close()


if __name__ == '__main__':
    main()


# Test
# array = []
# tester = CreditCard("Keith", 12.99, array, "test2", "test3", "test4")


# print(tester.benefits)
