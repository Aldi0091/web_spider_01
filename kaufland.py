import csv
import openpyxl
import os
import requests
from bs4 import BeautifulSoup


class KaufLand:
    @classmethod
    def kaufland(cls):
        abspath = os.getcwd()
        headers = None

        euro_to_czk_url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=CZK"

        res = requests.get(euro_to_czk_url)

        with open("euro_to_czl_2.html", "w") as file:
            file.write(res.text)

        with open("euro_to_czl_2.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        result = soup.find("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
        currency_euro_to_czk = round(float(result.split()[0]), 2)

        ########################################################################################################
        # HERE YOU SET THE +% REVENUE VALUE
        revenue = 1.0

        workbook = openpyxl.load_workbook("updated.xlsx")
        worksheet = workbook.active

        new_header = [
            "ean",
            "condition",
            "price",
            "currency",
            "id_warehouse",
            "count",
            "price_cs",
            "handling_time"
        ]

        rix = []
        rix.append(new_header) 
        for row in worksheet:
            listing = ["", "", "", "", "", "", "", ""]
            if str(row[0].value) != "sku" and len(str(row[0].value)) == 6:
                listing[0] = str(row[1].value)
                listing[1] = ''
                listing[2] = str(int(((float(row[2].value) / currency_euro_to_czk)*revenue)))
                listing[3] = currency_euro_to_czk
                listing[4] = str(row[0].value)
                listing[5] = row[3].value

                rix.append(listing)
            
        with open(f'{abspath}/feeds/kaufland-de updated.csv', "a") as f:
            writer = csv.writer(f)
            for row in rix:
                writer.writerow(row)


    