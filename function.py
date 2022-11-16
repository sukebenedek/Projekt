from results import Result1, Result2

results = []

def readFile():
    results.clear()
    f = open('ecdl.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result1(row.strip())
        results.append(r)
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
    f = open('ecdl.csv', 'a', encoding='UTF=8')
    f.write(row)
    f.close()

    r = Result1(row)
    results.append(r)


def writeFile():
    results.clear()
    f = open('ecdl.csv', 'w', encoding='UTF=8')
    for r in results:
        row = f'{r.name};{r.allPrice};{r.partPrice}\n' 
        f.write(row)
    f.close()

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


def lists():
    for i in results:
        print(f'{i.name}:\t {i.allPrice} {i.partPrice}/db\n')
    input('')

# 2 -----------------------------------------------------------------------------------------------------------------------

results2 = []

def readFile2():
    results2.clear()
    f = open('ecdl2.csv', 'r', encoding='UTF=8')
    for row in f:
        r = Result2(row.strip())
        results2.append(r)
    f.close()



def searchByName2():
    name = input('Név(Részlet): ')
    for r in results2:
        if name.lower() in r.name2.lower():
            print(f'{r.name2} {r.allPrice2}: {r.partPrice2} db')
        
    input('\n')


def newResults2():
    name = input('Név(Részlet): ')
    allPrice = input('Modul: ')
    time = input('Idő (óó:pp): ')
    partPrice = int(input('Százalék: '))

    row = f'{name2};{allPrice2};{partPrice2}\n'
    f = open('ecdl2.csv', 'a', encoding='UTF=8')
    f.write(row)
    f.close()

    r = Result2(row)
    results2.append(r)


def writeFile2():
    results2.clear()
    f = open('ecdl2.csv', 'w', encoding='UTF=8')
    for r in results2:
        row = f'{r.name2};{r.allPrice2};{r.partPrice2}\n' 
        f.write(row)
    f.close()

def deleteResults2():
    name = input('Név: ')
    for r in results2:
        if r.name2.lower() == name.lower():
            results2.remove(r)
            writeFile2()
            return
    input('Ilyen nevű vizsgázó nem volt')


def modifyResults2():
    name = input('Név: ')
    for r in results2:
        if r.name2.lower() == name.lower():
            # index = results2.index(r)    # r elem indexe a results2 listában
            r.time = input('Idő (óó:pp): ')
            r.partPrice = int(input('Százalék: '))
            writeFile()
            return

    input('Ilyen nevű vizsgázó nem volt')


def ownList():
    for i in results2:
        print(f'{i.name2}:\t {i.allPrice2} {i.partPrice2}/db\n')
    input('')

    
# 1,2 -------------------------------------------------------------------------------------------------------------------


def buy():
    num = 1
    name = input('Név: ')
    for i in results:
        if name.lower() in i.name.lower():
            print('Ilyen nincs de lehet ezekre gondoltál')
            print(f'{num}.{i.name}:\t {i.allPrice} {i.partPrice}/db')
        elif name.lower() == i.name.lower():
            count = input('Mennyit szeretne venni belőle?: ')
            for i in result2:
                if name.lower() == i.name2.lower():
                    i.allPrice2 += int(count)
                    for i in results:
                        i.allPrice -= int(count)

            
    