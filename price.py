from feeds import Eprice, KaufLand, Allegro


async def price(rate, revenue):

    Eprice.eprice(rate, revenue)
    KaufLand.kaufland(rate, revenue)
    Allegro.allegro(rate, revenue)





