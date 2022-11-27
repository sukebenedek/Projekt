
class Result1:


    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.allPrice = int(data[1])
        self.partPrice = data[2]


class Result2:


    def __init__(self, row: str):
        data = row.split(';')
        self.name2 = data[0]
        self.allPrice2 = int(data[1])
        self.partPrice2 = data[2]


class Result3:


    def __init__(self, row: str):
        data = row.split(';')
        self.name3 = data[0]
        self.allPrice3 = int(data[1])
        self.partPrice3 = data[2]


class szorzo:


    def __init__(self, row: str):
        data = row.split(';')
        self.MyData = data[0]

class Cash:


    def __init__(self, row: str):
        data = row.split(';')
        self.MyCash = int(data[0])
