import aiohttp
from aiohttp import ClientSession
import asyncio
import os


class Web:

    def __init__(self, url_list):
        self.url_list = url_list

    async def gather_with_concurr(self, n: int, *tasks):
        """Takes number for semaphore and awaitable tasks and returns response list"""
        semaphore = asyncio.Semaphore(n)
        async def sem_task(task):
            async with semaphore:
                return await task
        return await asyncio.gather(*(sem_task(task) for task in tasks))


    async def get_async(self, url: str, session: ClientSession):
        """A method for returning the raw response string"""
        async with session.get(url) as response:
            return [await response.text(), response.url]

    async def get_web(self):
  
        conn = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300)
        async with aiohttp.ClientSession(connector=conn) as session:
            res = await self.gather_with_concurr(300, *[self.get_async(i, session) for i in self.url_list])
            return res

    async def main(self) -> list:
        """The main function that generates the aiohttp session and fetch data from urls for further formatting"""
        result = await self.get_web()
        absolutepath = os.getcwd()
        if not os.path.exists(f"{absolutepath}/shop"): # /home/aldo/SCRAPING/CZ
            os.makedirs(f"{absolutepath}/shop")

        for res in result:
            html_body = str(res[0])
            url = str(res[1])
            x = len("https://www.czc.cz/")
            y = url.index("produkt")
            with open(f"/home/aldo/SCRAPING/CZ/shop/{url[x:(y-1)].replace('/', '_')}.html", "w") as file:
                file.write(html_body)


