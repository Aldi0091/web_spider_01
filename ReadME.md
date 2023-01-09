> We will need a web interface where I will upload a file with the product reference (SKU) so the spider will check each product to get stock availability and price tax excluded and included

> I will supply server to host the app and whatever is needed, the spider has to be customizable to scrape data (still stock availability and price) from a second website.

> The spider has to login to the website with my credentials.

> The expected output is a csv or xlsx file with data.

> The script has to come with a changelog file because will be modified in the future so who will have the job will have to mantain the script as well.

What we need is a backend dashboard where we can upload the csv file with the list of products and URL to retrieve them, this file will tell the spider where to crawl the info

Than we will have 1 or more CSV file that has to be updated with the data that spider has crawled, those files are feeds that will than be pushed via API to the destination marketplace.

As we are based in Czech republic our currency is Czech krown, so we need to have some field where the spider will get the conversion rate of the day to convert price in Euro or other currency according to destination marketplace

Example:
Feed A has destination marketplace X in Euro
Feed B has destination marketplace Y in RON
Feed C has destination marketplace W in Zloty
Feed D has destination marketplace Z in USD

So via dashboard we will load a starting file to check availability and price, than spider will save the data in all the feeds according to different fields per feeds and will adjust the cost with the price + x% (variable for every marketplace)

-------------------------------------------------------------------------------------------------------

> ORIGINALE.xlsx is the file that will be used by crawler to update quantity and price

> The other are the feed that the second automation will populate with the data got from the crawler, adjustiung the currency exchange, the files are here below exlained

> eprice feed.csv is the feed file for marketplace www.eprice.it, based on Mirakl as platform (https://www.mirakl.com/)

> kaufland-de.csv is the feed for marketplace www.kaufland.de and I think is a custom solution but they have documentation here: https://sellerapi.kaufland.com/

> Than there will be kaifland-sk.csv that will be the feed for the slovak sales channel of kaufland, so the API are the same

> sddone_allegro.xlsm is the feed file for www.allegro.pl that doesn't have API because has to be manipulated manually for submission.

> Than there will be the feed for rumenian marketplace www.emag.ro and they use a custoim platform as well but API documentation is here: https://marketplace.emag.ro/infocenter/emag-academy/product-import-through-api-or-feeds/?lang=en

> Still are missing API for cdiscount.fr marketplace because they still have to accept our submission and more marketplaces to come

> As you can see every file is a feed for a different marketplace with dufferent API, that's because we need the changelog files, because you will be in charge to mantain the script even with future marketplace

> Summary:
> 1st script is the real creawler that will read data from website czc.cz and will update quantity and price on file ORIGINALE.xlsx
> 2nd script will be an automation that will read data from ORIGINALE.xlsx and write data (quantity and converted price) in each feed

