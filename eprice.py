import csv
import openpyxl
import os
import requests
from bs4 import BeautifulSoup

abspath = os.getcwd()
headers = None

euro_to_czk_url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=CZK"

res = requests.get(euro_to_czk_url)

with open("euro_to_czl.html", "w") as file:
    file.write(res.text)

with open("euro_to_czl.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

result = soup.find("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
currency_euro_to_czk = float(result.split()[0])

# HERE YOU SET THE +% REVENUE VALUE
revenue = 1.0

workbook = openpyxl.load_workbook("updated.xlsx")
worksheet = workbook.active

rix = []
for row in worksheet:
    with open(f'{abspath}/feeds/eprice feed.csv', "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        for r in reader:
            x = r[0].split(";")
            if x[0] in str(row[0].value) and len(x) == 19:
                x[5] = str(round(((float(row[2].value) / currency_euro_to_czk)*revenue), 2))
                x[7] = row[3].value
                rix.append(x)
                break
            
with open(f'{abspath}/feeds/eprice feed updated.csv', "a") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for row in rix:
        writer.writerow(row)


    