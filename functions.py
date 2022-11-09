from classs import Result

results = []

def readCompanies():
    f = open('companies.csv', 'r', encoding='UTF=8')
    # f.readline()
    for row in f:
        r = Result(row.strip())
        results.append(r)
    f.close()

readCompanies()

def writeFile():
    f = open("companies.csv", "w", encoding="UTF-8")
    # open("filename", "w").close()
    for r in results:
        row = f'{r.name};{r.allPrices};{r.oneStockPrice}\n'
        f.write(row)
    f.close()

def oneStockPriceCalculator():
    # f = open("companies.csv", "a", encoding="UTF-8")
    for r in results:
        r.oneStockPrice = r.allPrices / 1000000000
    writeFile()
    return
oneStockPriceCalculator()
readCompanies()    


# for i in results:
#     print(i.name, i.percent)7





# for i in range(len(results)):
#     print(results[i].oneStockPrice)

def toDollar(num):
    if num > 100000000000:
        return f"${num / 100000000000} T"
    elif num > 100000000:
        return f"${num / 100000000} B"
    elif num > 100000:
        return f"${num / 100000} M"
    else:
        return f"${num}"



