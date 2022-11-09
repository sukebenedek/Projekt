class Result:
    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.allPrices = int(data[1])
        self.oneStockPrice = data[2]