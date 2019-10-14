from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
# URLs to scrape through
url = [
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
# "https://creditcards.chase.com/rewards-credit-cards/disney-rewards?CELL=6TKX",
# "https://creditcards.chase.com/travel-credit-cards/ihg-rewards-club-premier?CELL=6TKX",
# "https://creditcards.chase.com/rewards-credit-cards/starbucks-rewards?CELL=6TKX",
# "https://creditcards.chase.com/cash-back-credit-cards/amazon-rewards?CELL=6TKX",
# "https://creditcards.chase.com/small-business-credit-cards/ink-unlimited?CELL=6TKX",
# "https://creditcards.chase.com/small-business-credit-cards/ink-cash?CELL=6TKX",
# "https://creditcards.chase.com/small-business-credit-cards/ink-business-preferred?CELL=6TKX",
# "https://www.americanexpress.com/us/credit-cards/card/gold-card/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-GoldCard",
# "https://www.americanexpress.com/us/credit-cards/card/platinum-delta-skymiles/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-DeltaPlatinum",
# "https://www.americanexpress.com/us/credit-cards/card/amex-everyday/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-AED",
# "https://www.americanexpress.com/us/credit-cards/card/platinum/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-Platinum",
# "https://www.americanexpress.com/us/credit-cards/card/blue-cash-everyday/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-BCE",
# "https://www.americanexpress.com/us/credit-cards/card/hilton-honors-surpass/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-HiltonSurpass",
# "https://www.americanexpress.com/us/credit-cards/card/blue-cash-preferred/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-BCP",
# "https://www.americanexpress.com/us/credit-cards/card/marriott-bonvoy-brilliant/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-MarriottBonvoyBrilliant",
# "https://www.americanexpress.com/us/credit-cards/card/cash-magnet/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-CashMagnet",
# "https://www.americanexpress.com/us/credit-cards/card/amex-everyday-preferred/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-AEDP",
# "https://www.americanexpress.com/us/credit-cards/card/delta-skymiles/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-DeltaGold",
# "https://www.americanexpress.com/us/credit-cards/card/hilton-honors-aspire/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-HiltonAspire",
# "https://www.americanexpress.com/us/credit-cards/card/hilton-honors/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-HiltonHonors",
# "https://www.americanexpress.com/us/credit-cards/card/delta-blue/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-DeltaBlue",
# "https://www.americanexpress.com/us/credit-cards/card/delta-reserve/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-DeltaReserve",
# "https://www.americanexpress.com/us/credit-cards/card/blue/?eep=25330&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-Blue",
# "https://www.capitalone.com/credit-cards/venture/",
# "https://www.capitalone.com/credit-cards/ventureone/",
# "https://www.capitalone.com/credit-cards/savor-dining-rewards/",
# "https://www.capitalone.com/credit-cards/savorone-dining-rewards/"
]

# CLass for credit card
class CreditCard:
    # There could be so many perks to havig a credit card
    def __init__(self, name, benefits, *options):
        self.name = name
        self.benefits = []
        self.benefits.append(options)

cardArray= []
for data in url:
    response = requests.get(data)
    page = urlopen(data)
    soup = BeautifulSoup(page, "html.parser")
    text = soup.get_text()

    titlebox = soup.find("h1", attrs = {'class', "card-title"})
    benefitsbox = soup.find("div", attrs = {'class', "primary-item"})
    title = titlebox.text.strip()
    benefits = benefitsbox.text().strip()
    card = CreditCard(title, cardArray, benefits)
    # TODO STORE IN SQL DATABASE


print(cardArray)




# Test
# array = []
# tester = CreditCard("Keith", 12.99, array, "test2", "test3", "test4")


# print(tester.benefits)
