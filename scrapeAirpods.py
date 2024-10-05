# TODO 4 - Save all rows to excel file
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"

HEADERS = {
"Accept-Language": ACCEPT_LANGUAGE,
"User-Agent": USER_AGENT
}

# TODO 1 - Open amazon search link and parse it
URL = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=airpods&_sacat=0"
response = requests.get(URL,HEADERS)
site = response.text
newSoup = BeautifulSoup(site,"html.parser")
print(newSoup.prettify())
# TODO 2 - Create new excel file with two columns - title and rating
#spreadsheet = Workbook()
#sheet = spreadsheet.active
#sheet["A1"] = "Title"
#sheet["B1"] = "Rating"
#spreadsheet.save('excelAirpods.xlsx')
# TODO 3 - Parse html file to get title and rating of the product
#productTag
"""productTag = newSoup.find_all(name="div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small gsx-ies-anchor sg-col-12-of-16")
for product in productTag:
    product.find(name="a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    print(product.getText())
"""