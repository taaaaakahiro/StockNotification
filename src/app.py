import openpyxl
import requests
from bs4 import BeautifulSoup

ASNI = 'B08GGGBKRQ'

url = 'http://amazon.jp/dp/' + ASNI
print(url)
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
txt = soup.select('#outOfStock > div > div.a-section.a-spacing-small.a-text-center > span.a-color-price.a-text-bold')
print(txt)