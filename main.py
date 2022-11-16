from function import ownList, lists, deleteResults, modifyResults, newResults, readFile, searchByName, readFile2, buy
from menu import menu


readFile()
readFile2() 
choice = menu()
while choice != 0:
    if choice == 1:
        ownList()
    if choice == 2:
        lists()
    if choice == 3:
        buy()
    if choice == 4:
        searchByName()
    choice = menu()