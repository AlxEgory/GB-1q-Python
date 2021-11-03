import requests
import xml.etree.ElementTree as ET
from decimal import Decimal


def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(response.text)
    for valute in root.findall('Valute'):
        if valute.find('CharCode').text == cur.upper():
            return Decimal(valute.find('Value').text.replace(',', '.'))
