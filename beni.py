from classs import *
from function import *
from functions import *


sorszam = 1
for row in results:
    
    print(f"{sorszam}. {row.name} \nÖsszérték {toDollar(row.allPrices)}\tEgy részvény ára: {toDollar(row.oneStockPrice)}\n-------------------------------------------------")


    sorszam += 1

def priceChangeSummary():
    for i in range()