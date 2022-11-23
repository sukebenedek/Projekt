from results import Result1, Result2, Result3, szorzo
import random


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

def readFile2():
    results2.clear()
    f = open('companies2.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result2(row.strip())
        results2.append(r)
    f.close()


def writeFile2():
    f = open('companies2.csv', 'w', encoding='UTF=8')
    for r in results2:
        row = f'{r.name2};{r.allPrice2};{r.partPrice2}\n' 
        f.write(row)
    f.close()


def ownList():
    readFile2()
    for i in results2:
        print(f'{i.name2}:\t {i.allPrice2} {i.partPrice2}$/db\n')
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
    for i in results3:
        print(f'{i.name3}:\t {toDollar(i.allPrice3)} | {i.partPrice3}$/db\n')
    input('')


# szorzok ---------------------------------------------------------------------------------------------------------------

szorzook = []

def readFileSZ():
    szorzook.clear()
    f = open('szorzok.csv', 'r', encoding='UTF=8')
    for row in f:
        r = szorzo(row.strip())
        szorzook.append(r)
    f.close()

def writeFileSZ():
    f = open('szorzok.csv', 'w', encoding='UTF=8')
    for r in szorzook:
        row = f'{r.data}\n' 
        f.write(row)
    f.close()

def writeFileSZDelet():
    szorzook.clear()
    f = open('szorzok.csv', 'w', encoding='UTF=8')
    for r in szorzook:
        row = f'{r.data}\n' 
        f.write(row)
    f.close()


# def beszorzas():
#     writeFileSZDelet()
#     for i in results3:
#         name = i.name3
#         alleprice3 = i.allPrice3
#         data = random.randint(95, 105)
#         a = data
#         data2 = int(data) / 100
#         row = f'{data2}\n'
#         f = open('szorzok.csv', 'a', encoding='UTF=8')
#         f.write(row)
#         f.close()
#         print(i.allPrice3)
#         print(alleprice3)
#         print(data)     
#         i.allPrice3 = int(alleprice3 * a / 100)
#         writeFile3()
#         for i in results:
#             if name.lower() == i.name.lower():
#                 alleprice = i.allPrice
#                 i.allPrice = int(alleprice * a / 100)  
#                 writeFile()
#                 for i in results2:
#                     if name.lower() == i.name2.lower():
#                         alleprice2 = i.allPrice2
#                         i. allPrice2 = alleprice2 * a / 100
#                         writeFile2() 
    

# 1,2 -------------------------------------------------------------------------------------------------------------------

def buySell():
    print('1. Ha eladni szeretnél')
    print('2. Ha vásárolni szeretnél')
    choice = input('Válaszd ki melyiket szeretnéd: ')
    while len(choice) != 1 or choice < '1' or choice > '2':
        choice = input('Válaszd ki melyiket szeretnéd: ')
    if choice == '1':
        sell()
    elif choice == '2':
        buy()
        
        


def buy():
    num = 1
    name = input('Név: ')
    for i in results:
        if name.lower().strip() == i.name.lower().strip():
            chname = i.name.strip()
            print(f'Maximum {i.allPrice} dollárnyi részesedést vehetsz')
            count = input('Mennyit szeretne venni belőle?(dollár): ')
            while int(count) > i.allPrice:
                print('Ha nem akarsz mégse venni(0)')
                count = input('Ennyi részesedés nem áll rendelkezésre adj meg kevesebb értéket: ')
                if count == 0:
                    return
            for i in results2:
                if name.lower() == i.name2.lower().strip():
                    i.allPrice2 += int(count)
                    i.partPrice2 = 0
                    writeFile2()
                    for i in results:
                        if name.lower() == i.name.lower().strip():
                            i.allPrice -= int(count)
                            writeFile()
                            return
                elif name.lower() != i.name2.lower().strip():
                    name = chname
                    allPrice = int(count)
                    partPrice = 0
                    row = f'{name};{allPrice};{partPrice}\n'
                    f = open('companies2.csv', 'a', encoding='UTF=8')
                    f.write(row)
                    f.close()
                    for i in results:
                        if name.lower().strip() == i.name.lower().strip():
                            i.allPrice -= int(count)
                            writeFile()
                            return
        elif name.lower().strip() in i.name.lower().strip():
            print('Ilyen nincs de lehet ezekre gondoltál')
            print(f'{num}.{i.name}:\t {i.allPrice} {i.partPrice}/db')
            input('')
            num += 1


def sell():
    num = 1
    name = input('Név: ')
    for i in results2:
        if name.lower().strip() == i.name2.lower().strip():
            count = input('Mennyit szeretne eladni belőle?(dollár): ')
            while int(count) > i.allPrice:
                count = input('Ennyi részesedés nincs nálad adj meg kevesebb értéket: ')
            for i in results:
                if name.lower().strip() == i.name.lower().strip():
                    i.allPrice += int(count)
                    i.partPrice = 0
                    writeFile()
                    for i in results2:
                        if name.lower().strip() == i.name2.lower().strip():
                            i.allPrice2 -= int(count)
                            writeFile2()
                            return
                else:
                    print('Ilyen nevű cégtől nincs részvényed')
        elif name.lower().strip() in i.name2.lower().strip():
            print('Ilyen nincs de lehet ezekre gondoltál')
            print(f'{num}.{i.name2}:\t {i.allPrice2} {i.partPrice2}/db')
            input('')
            num += 1


def oneCal():
    for i in results3:
        i.partPrice3 = i.allPrice3 / 1000000000
        writeFile3()
            
def toDollar(num):
    if num > 100000000000:
        return f"${num / 100000000000} T"
    elif num > 100000000:
        return f"${num / 100000000} B"
    elif num > 100000:
        return f"${num / 100000} M"
    else:
        return f"${num}"

        
                        
    
                        
                         

                    
                    
                

            
    