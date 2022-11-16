
class Result1:


    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.allPrice = data[1]
        self.partPrice = data[2]


class Result2:


    def __init__(self, row: str):
        data = row.split(';')
        self.name2 = data[0]
        self.allPrice2 = data[1]
        self.partPrice2 = data[2]  