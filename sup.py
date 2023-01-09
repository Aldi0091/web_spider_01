from bs4 import BeautifulSoup

class DirectParse:

    @classmethod
    def get_produkt_info(cls, url):
        x = len("https://www.czc.cz/")
        y = url.index("produkt")
        with open(f"/home/aldo/SCRAPING/CZ/shop/{url[x:(y-1)].replace('/', '_')}.html") as file:
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
        # print(result.text.strip()) # .text.strip()
        # print(cena_bez_vat.text.strip())
        # print(cena_with_vat.text.strip())
        return {
            "quantity": result.text.strip().replace(u'\xa0', u' '), 
            "price without VAT": cena_bez_vat.text.strip().replace(u'\xa0', u' '),
            "price with VAT": cena_with_vat.text.strip().replace(u'\xa0', u' ')
        }

    
    
        # try:
        #     result = soup.find("span", class_="availability-long-term")
        #     try:
        #         cenovoe = soup.find_all("span", class_="price action")
        #         for cena in cenovoe:
        #                 cena_bez_vat = cena.find("span", class_="price-vatex")
        #                 cena_with_vat = cena.find("span", class_="price-vatin")
        #         if cenovoe == None:
        #             raise Exception("no price")
        #     except Exception:
        #         cenovoe = soup.find_all("span", class_="price alone")
        #         for cena in cenovoe:
        #                 cena_bez_vat = cena.find("span", class_="price-vatex")
        #                 cena_with_vat = cena.find("span", class_="price-vatin")
        #     if result == None:
        #         raise Exception("result is not found 4")
        # except Exception:
        #     try:
        #         result = soup.find("span", class_="stores-and-delivery availability-state-on-stock")
        #         cenovoe = soup.find_all("span", class_="price alone")
        #         for cena in cenovoe:
        #             cena_bez_vat = cena.find("span", class_="price-vatex")
        #             cena_with_vat = cena.find("span", class_="price-vatin")
        #         if result == None:
        #             raise Exception("result is not found 1")
        #     except Exception:
        #         try:
        #             result = soup.find_all("span", class_="stores-and-delivery availability-state-external-storage")
        #             cenovoe = soup.find_all("span", class_="price")
        #             for cena in cenovoe:
        #                 cena_bez_vat = cena.find("span", class_="price-vatex")
        #                 cena_with_vat = cena.find("span", class_="price-vatin")
        #                 break
        #             if result == None:
        #                 raise Exception("result is not found 3")
        #         except Exception:
        #             result = soup.find_all("span", class_="availability-state-not-on-stock")
        #             cenovoe = soup.find_all("span", class_="price alone")
        #             for cena in cenovoe:
        #                 cena_bez_vat = cena.find("span", class_="price-vatex")
        #                 cena_with_vat = cena.find("span", class_="price-vatin")
        #             if result == None:
        #                 raise Exception("result is not found 2")
                
        

# class Sup:

#     def __init__(self, sku):
#         self.sku =sku

#     def find_link(self):
#         with open(f"/home/aldo/SCRAPING/CZ/pages/{self.sku}.html") as file:
#             src = file.read()

#         soup = BeautifulSoup(src, "lxml")

#         result = soup.find_all("a", href=True)
#         print(result)
#         for r in result:
#             lin = r.get('href')
#             if "url?q=https://www.czc.cz" in lin:
#                 if str(self.sku) in lin:
#                     if "produkt" in lin:
#                         lin = r.get('href')
#                         start = lin.index("http")
#                         end = lin.index("produkt") + len("produkt")
#                         return lin[start:end]
                    






                

