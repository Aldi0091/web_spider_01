from bs4 import BeautifulSoup
import os


class DirectParse:

    @classmethod
    def get_produkt_info(cls, url):
        x = len("https://www.czc.cz/")
        y = url.index("produkt")
        absolutepath = os.getcwd()
        with open(f"{absolutepath}/shop/{url[x:(y-1)].replace('/', '_')}.html") as file: # /home/aldo/SCRAPING/CZ
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        status_at_warehouse = [
            "availability-long-term",
            "stores-and-delivery availability-state-on-stock",
            "stores-and-delivery availability-state-external-storage",
            "availability-state-not-on-stock",
            "stores-and-delivery availability-state-for-order"
        ]
        cena_bez_vat, cena_with_vat = None, None
        results = [soup.find("span", class_=f"{state}") for state in status_at_warehouse]
        for res in results:
            if res != None:
                result = res
                break
        prices = soup.find_all("span", class_="price alone")
        for price in prices:
            cena_bez_vat = price.find("span", class_="price-vatex")
            cena_with_vat = price.find("span", class_="price-vatin")
        if (cena_bez_vat == None) or (cena_with_vat == None):
            prices = soup.find_all("span", class_="price action")
            for price in prices:
                cena_bez_vat = price.find("span", class_="price-vatex")
                cena_with_vat = price.find("span", class_="price-vatin")
            if (cena_bez_vat == None) or (cena_with_vat == None):
                prices = soup.find_all("span", class_="price")
                for price in prices:
                    cena_bez_vat = price.find("span", class_="price-vatex")
                    cena_with_vat = price.find("span", class_="price-vatin")
                    break
        return {
            "quantity": result.text.strip().replace(u'\xa0', u' '), 
            "price without VAT": cena_bez_vat.text.strip().replace(u'\xa0', u' '),
            "price with VAT": cena_with_vat.text.strip().replace(u'\xa0', u' ')
        }

