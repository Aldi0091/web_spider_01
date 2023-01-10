from async_sup import DirectParse
from async_fetch import Web
from urls import Url
import asyncio, logging
from feeds import Eprice, KaufLand, Allegro

# logging.basicConfig(filename="sample.log", level=logging.INFO)
# logger = logging.getLogger()

# revenue = 1.0 # this is multiplier *% for final price at marketplace

async def update(path):
    address = path
    empty_dict = dict()
    all_urls_list = Url(address, empty_dict).collect_all_urls()
    await Web(all_urls_list).main()
    # logger.info("fetched web pages and saved to /shop/*.html")
    ret = await DirectParse.get_tasks(all_urls_list)
    Url(address, ret).update_sheet()







