from async_sup import DirectParse
from async_fetch import Web
from urls import Url
import asyncio
import logging
from eprice import Eprice
from kaufland import KaufLand
from allegro import Allegro

logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger()


async def retting():
    address = "ORIGINALE.xlsx" 
    empty_dict = dict()
    all_urls_list = Url(address, empty_dict).collect_all_urls()
    await Web(all_urls_list).main()
    logger.info("fetched web pages and saved to /shop/*.html")
    ret = await DirectParse.get_tasks(all_urls_list)
    Url(address, ret).update_sheet()
    Eprice.eprice()
    KaufLand.kaufland()
    Allegro.allegro()

asyncio.run(retting())



