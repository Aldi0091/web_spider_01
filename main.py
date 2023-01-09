from sup import DirectParse
from async_fetch import Web
from urls import Url
import asyncio
import logging
from eprice import Eprice
from kaufland import KaufLand
from allegro import Allegro

logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger()
address = "ORIGINALE.xlsx" 
empty_dict = dict()


all_urls_list = Url(address, empty_dict).collect_all_urls()

asyncio.run(Web(all_urls_list).main())
logger.info("fetched web pages and saved to /shop/*.html")

outcome = dict()
counter = 0
for sku in all_urls_list:
    logger.info(f"scraping the web page for data: {sku}")
    counter += 1
    print(f"INFO: PLEASE WAIT UNTIL COMPLETE {len(all_urls_list) - counter}")
    ret = DirectParse.get_produkt_info(sku)
    outcome[sku] = ret
Url(address, outcome).update_sheet()

Eprice.eprice()
KaufLand.kaufland()
Allegro.allegro()
