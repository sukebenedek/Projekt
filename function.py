from results import Result1, Result2, Result3, szorzo, Cash
import random
import os
# from menu import menu
# from date import lastJump

results = []

def readFile():
    results.clear()
    f = open('companies.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result1(row.strip())
        results.append(r)
    f.close()

def writeFile():
    f = open('companies.csv', 'w', encoding='UTF=8')
    for r in results:
        row = f'{r.name};{r.allPrice};{r.partPrice}\n' 
        f.write(row)
    f.close()



def searchByName():
    name = input('Név(Részlet): ')
    for r in results:
        if name.lower() in r.name.lower():
            print(f'{r.name} {r.allPrice}: {r.partPrice} db')
        
    input('\n')


def newResults():
    name = input('Név(Részlet): ')
    allPrice = input('Modul: ')
    time = input('Idő (óó:pp): ')
    partPrice = int(input('Százalék: '))

    row = f'{name};{allPrice};{time};{partPrice}\n'
    f = open('companies.csv', 'a', encoding='UTF=8')
    f.write(row)
    f.close()

    r = Result1(row)
    results.append(r)


def deleteResults():
    name = input('Név: ')
    for r in results:
        if r.name.lower() == name.lower():
            results.remove(r)
            writeFile()
            return
    input('Ilyen nevű vizsgázó nem volt')


def modifyResults():
    name = input('Név: ')
    for r in results:
        if r.name.lower() == name.lower():
            # index = results.index(r)    # r elem indexe a results listában
            r.time = input('Idő (óó:pp): ')
            r.partPrice = int(input('Százalék: '))
            writeFile()
            return

    input('Ilyen nevű vizsgázó nem volt')



# 2 -----------------------------------------------------------------------------------------------------------------------

results2 = []
listOfNevek = []

def readFile2():
    results2.clear()
    f = open('companies2.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result2(row.strip())
        results2.append(r)

        rowadikNev = row.replace("\n", "")
        rowadikNevList = rowadikNev.split(";")
        if rowadikNevList[0] not in listOfNevek:
            listOfNevek.append(rowadikNevList[0].lower())
    f.close()


def writeFile2():
    f = open('companies2.csv', 'w', encoding='UTF=8')
    for r in results2:
        row = f'{r.name2};{r.allPrice2};{r.partPrice2}\n' 
        f.write(row)
    f.close()


def ownList():
    readFile2()
    print(f"Saját részvényeid({len(results2)} db):\n")
    for i in results2:
        print(f'{i.name2}:\t {i.allPrice2}$\n')
    input('')
#3 ----------------------------------------------------------------------------------------------------------------------

results3 = []

def readFile3():
    results3.clear()
    f = open('companies3.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result3(row.strip())
        results3.append(r)
    f.close()

    

def writeFile3():
    f = open('companies3.csv', 'w', encoding='UTF=8')
    for r in results3:
        row = f'{r.name3};{r.allPrice3};{r.partPrice3}\n' 
        f.write(row)
    f.close()


def lists():
    hanyadik = 0
    for i in results3:
        # print(f'{i.name3}:\t {toDollar(i.allPrice3)} | {i.partPrice3}$/db\n')
        print(f"{hanyadik + 1}.\tNév: {i.name3}")
        print(f"Összes piaci érték: {toDollar(i.allPrice3)}")
        oneStockPrice = "{:.2f}".format(float(i.partPrice3))
        print(f"Egy részvény ára: {toDollar(oneStockPrice)}")
        if i.name3.lower() in listOfNevek:
            print(f"\nBirtokolsz ilyen részvényt.")
        print('\n---------------------------------')
        hanyadik += 1
    input('')


# szorzok ---------------------------------------------------------------------------------------------------------------

szorzook = []
listOfSzorzok = []

def readFileSZ():
    szorzook.clear()
    f = open('szorzok.csv', 'r', encoding='UTF=8')
    for row in f:
        r = szorzo(row.strip())
        szorzook.append(r)

        rowadikSzorzo = row.replace("\n", "")
        listOfSzorzok.append(float(rowadikSzorzo))
    f.close()

def writeFileSZ():
    f = open('szorzok.csv', 'w', encoding='UTF=8')
    for r in szorzook:
        row = f'{r.MyData}\n' 
        f.write(row)
    f.close()

def writeFileSZDelet():
    szorzook.clear()
    f = open('szorzok.csv', 'w', encoding='UTF=8')
    for r in szorzook:
        row = f'{r.MyData}\n' 
        f.write(row)
    f.close()



# cash ------------------------------------------------------------------------------------------------------------------

money =[]

def readFileC():
    money.clear()
    f = open('cash.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Cash(row.strip())
        money.append(r)
    f.close()


def writeFileC():
    f = open('cash.csv', 'w', encoding='UTF=8')
    for r in money:
        row = f'{r.MyCash}\n' 
        f.write(row)
    f.close()

def Mymoney():
    for i in money:
        return(i.MyCash)

# 1,2 -------------------------------------------------------------------------------------------------------------------

def buySell():
    print('1. Ha eladni szeretnél.')
    print('2. Ha vásárolni szeretnél.')
    print('\n0. Ha ki szeretnél lépni.\n')
    choice = input('Válaszd ki melyiket szeretnéd: ')
    if choice == '1':
        sell()
    elif choice == '2':
        buy()
    elif choice == '0':
        return
    else:
        print("\nIlyen menüpont nincs")
        input("")
        
        


def buy():
    readFile()
    readFile2()
    readFile3()
    num = 1
    name = input('Név: ')
    for i in results:
        if name.lower() == i.name.lower():
            chname = i.name
            print(f'Maximum {i.allPrice} dollárnyi részesedést vehetsz')
            count = input('Mennyit szeretne venni belőle?(dollár): ')
            for e in money:
                while e.MyCash < int(count):
                    count = input('Ennyi pénzed nincsen vegyél kevesebbet: ')
            while int(count) > i.allPrice:
                print('Ha nem akarsz mégse venni(0)')
                count = input('Ennyi részesedés nem áll rendelkezésre adj meg kevesebb értéket: ')
                if count == 0:
                    return
            for i in results2:
                if name.lower() == i.name2.lower():
                    i.allPrice2 += int(count)
                    i.partPrice2 = 0
                    writeFile2()
                    for i in results:
                        if name.lower() == i.name.lower():
                            i.allPrice -= int(count)
                            writeFile()
                            for i in money:
                                i.MyCash -= int(count)
                                writeFileC()
                                return
            number = 0
            while len(results2) < number and name.lower() != number.name2.lower():
                number += 1
            name = chname
            allPrice = int(count)
            partPrice = 0
            row = f'{name};{allPrice};{partPrice}\n'
            f = open('companies2.csv', 'a', encoding='UTF=8')
            f.write(row)
            f.close()
            for i in results:
                if name.lower() == i.name.lower():
                    i.allPrice -= int(count)
                    writeFile()
                    for i in money:
                        i.MyCash -= int(count)
                        writeFileC()
                        return
    print('Ilyen nincs de lehet ezekre gondoltál\n')
    # input('dadassd')
    for i in results3:
        if name.lower() in i.name3.lower():
            print(f'{num}.{i.name3}:\t {i.allPrice3} {i.partPrice3}/db')
            num += 1
    input('')


def sell():
    num = 1
    name = input('Név: ')
    for i in results2:
        if name.lower() == i.name2.lower():
            print(f'Maximum {i.allPrice2} dollárnyi részesedést adhatsz el.')
            count = input('Mennyit szeretne eladni belőle?(dollár): ')
            while int(count) > i.allPrice2:
                count = input('Ennyi részesedés nincs nálad adj meg kevesebb értéket: ')
            for i in results:
                if name.lower() == i.name.lower():
                    i.allPrice += int(count)
                    i.partPrice = 0
                    writeFile()
                    for i in results2:
                        if name.lower() == i.name2.lower():
                            i.allPrice2 -= int(count)
                            writeFile2()
                            for i in money:
                                i.MyCash += int(count)
                                writeFileC()
                                return
                else:
                    print('Ilyen nevű cégtől nincs részvényed')
    print('Ilyen nincs de lehet ezekre gondoltál\n')
    # input('dadassd')
    for i in results2:
        if name.lower() in i.name2.lower():
            print(f'{num}.{i.name2}:\t {i.allPrice2} {i.partPrice2}/db')
            num += 1
    input('')


def oneCal():
    for i in results3:
        i.partPrice3 = i.allPrice3 / 1000000000
        writeFile3()
            
def toDollar(num):
    num = float(num)
    if num > 100000000000:
        formattedNum = '{:.3f}'.format(num / 100000000000)
        return f"${formattedNum} T"
    elif num > 100000000:
        formattedNum = '{:.3f}'.format(num / 100000000)
        return f"${formattedNum} B"
    elif num > 100000:
        formattedNum = '{:.3f}'.format(num / 100000)
        return f"${formattedNum} M"
    else:
        formattedNum = '{:.2f}'.format(num)
        return f"${formattedNum}"
    
    
# 4 -----------------------------------------------------------------------------------------------------------------------
today = "2022-11-30"
today = today.split("-")
day = int(today[2])
month = int(today[1])
year = int(today[0])
date = today
a = None
data = None
listOfAllPrices = [] #azoknak az áraknak a listája amik még árváltozás előtt voltak

lastJump = ""

def jumpDate(howMuch):
    global day, month, year, date, lastJump
    if howMuch == "day":
        lastJump = "day"
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
        lastJump = "month"
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
    os.system("cls")
    print(f"Jelenlegi dátum {jumpDate(str())}\n")
    print(f"1. Egy nap ugrása az időben.\n2. Egy hónap ugrása az időben.\n\n0. Kilépés\n")

    jumpType = input("Választásod: ")
    print()

    listOfAllPrices = []

    for i in results3:
        listOfAllPrices.append(i.allPrice3)

    if jumpType == "1":
        date = jumpDate("day")
        print(f"Jelenlegi dátum: {date}\n")
    elif jumpType == "2":
        date = jumpDate("month")
        print(f"Jelenlegi dátum: {date}\n")
    elif jumpType == "0":
        return
    else:
        print("Ilyen választás nem létezik.\n")
        input()
        return

    writeFileSZDelet()

    print("Betöltés", end="")
    data = None
    for i in results3:              # data: random sorsolt százalékos szorzó
        name = i.name3              # data2: data float, használható formában / 100
        if jumpType == '1':
            alleprice3 = i.allPrice3
            data = random.randint(97, 103)
        elif jumpType == '2':
            alleprice3 = i.allPrice3
            data = random.randint(80, 120)
        else:
            timeJumping()
        a = data
        data2 = int(data) / 100
        row = f'{data2}\n'
        f = open('szorzok.csv', 'a', encoding='UTF=8')
        f.write(row)
        f.close()
        print(".", end="")
        # print(i.allPrice3)
        # print(alleprice3)
        # print(data)     
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
                        i.allPrice2 = alleprice2 * a / 100
                        writeFile2()
        oneCal()

    # beszorzas()
    os.system("cls")
    print(f"Jelenlegi dátum: {date}\n")
    input("")

# 5 -----------------------------------------------------------------------------------------------------------------------

def summaryAfterPriceChange():
    
    readFile2()
    readFileSZ()

    print(jumpDate(""))
    print("Árváltozás utáni összegzés\n")
    if lastJump == "":
        print("Eddig nem történt árváltozás.\n")
        # print(listOfNevek)    
    elif lastJump == "day":
        # print(szorzook)
        # print(listOfSzorzok)
        hanyadik = 0
        for i in results3:
            # print(f'{i.name3}:\t {toDollar(i.allPrice3)} | {i.partPrice3}$/db\n')
            print('----------------------------------------')
            print(f"Név: {i.name3}".center(40, "-"), end="\n\n")
            
            print(f"Összes piaci érték 1 napja: {toDollar(int(i.allPrice3) / listOfSzorzok[hanyadik])}")
            print(f"Egy részvény ára 1 napja: {toDollar(int(i.allPrice3) / listOfSzorzok[hanyadik] / 1000000000)}\n")

            print(f"Jelenlegi összes piaci érték: {toDollar(i.allPrice3)}")
            oneStockPrice = "{:.2f}".format(float(i.partPrice3))
            print(f"Jelenleg egy részvény ára: {toDollar(oneStockPrice)}\n")

            if float('{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)) == 0:
                print(f"Ennek a részvénynek az ára nem változott.\n")
            elif float('{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)) > 0:
                print(f"Ez a részvény {'{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)} százalékkal növekedett.\n")
            else: 
                print(f"Ez a részvény {'{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * -100)} százalékkal csökkent.\n")

            hanyadik += 1
    elif lastJump == "month":
        # print("honap")
        hanyadik = 0
        for i in results3:
            print('----------------------------------------')
            print(f"Név: {i.name3}".center(40, "-"), end="\n\n")
            
            print(f"Összes piaci érték 1 hónapja: {toDollar(int(i.allPrice3) / listOfSzorzok[hanyadik])}")
            print(f"Egy részvény ára 1 hónapja: {toDollar(int(i.allPrice3) / listOfSzorzok[hanyadik] / 1000000000)}\n")

            print(f"Jelenlegi összes piaci érték: {toDollar(i.allPrice3)}")
            oneStockPrice = "{:.2f}".format(float(i.partPrice3))
            print(f"Jelenleg egy részvény ára: {toDollar(oneStockPrice)}\n")

            if float('{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)) == 0:
                print(f"Ennek a részvénynek az ára nem változott.\n")
            elif float('{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)) > 0:
                print(f"Ez a részvény {'{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * 100)} százalékkal növekedett.\n")
            else: 
                print(f"Ez a részvény {'{:.1f}'.format((listOfSzorzok[hanyadik]- 1.0) * -100)} százalékkal csökkent.\n")

            hanyadik += 1
    else:
        print("Hiba kód: 001")

    input("")