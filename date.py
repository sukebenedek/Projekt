import os
from function import *

today = "2022-11-23"
today = today.split("-")
day = int(today[2])
month = int(today[1])
year = int(today[0])
date = today

def jumpDate(howMuch):
    global day, month, year, date
    if howMuch == "day":
        if month > 12:
            day = 1
            month = 1
            year += 1
        elif day == 30:
            day = 1
            month += 1
        elif day <= 29:
            day += 1
        if month == 13:
            jumpDate("day")

    if howMuch == "month":
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    

    # if howMuch == "":
    #     date = f"{year}-{month}-{day}"
    # date = f"{year}-{month}-{day}"
    return(f"{year}-{month}-{day}")


def timeJumping():
    
    print(f"Jelenlegi dátum {jumpDate(str())}")
    print(f"1. Egy nap ugrása az időben.\n2. Egy hónap ugrása az időben\n")

    jumpType = input("Választásod: ")
    print()

    if jumpType == "1":
        date = jumpDate("day")
        print(f"Jelenlegi dátum: {date}\n")
    elif jumpType == "2":
        date = jumpDate("month")
        print(f"Jelenlegi dátum: {date}\n")
    else:
        print("Ilyen választás nem létezik.\n")

    writeFileSZDelet()
    for i in results3:
        name = i.name3
        if jumpType == '1':
            alleprice3 = i.allPrice3
            data = random.randint(95, 105)
        elif jumpType == '2':
            alleprice3 = i.allPrice3
            data = random.randint(80, 120)
        a = data
        data2 = int(data) / 100
        row = f'{data2}\n'
        f = open('szorzok.csv', 'a', encoding='UTF=8')
        f.write(row)
        f.close()
        print(i.allPrice3)
        print(alleprice3)
        print(data)     
        i.allPrice3 = int(alleprice3 * a / 100)
        writeFile3()
        for i in results:
            if name.lower() == i.name.lower():
                alleprice = i.allPrice
                i.allPrice = int(alleprice * a / 100)  
                writeFile()
                for i in results2:
                    if name.lower() == i.name2.lower():
                        alleprice2 = i.allPrice2
                        i. allPrice2 = alleprice2 * a / 100
                        writeFile2()





    # beszorzas()
    os.system("cls")
    print(f"Jelenlegi dátum: {date}\n")
    input("Ok")

    