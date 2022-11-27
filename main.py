from function import ownList, lists, deleteResults, modifyResults, newResults, readFile, readFile2, readFile3,readFileC, searchByName, buySell, oneCal 
from menu import menu
from date import *


readFile()
readFile2() 
readFile3()
readFileC()
choice = menu()
while choice != 0:
    if choice == 1:
        ownList()
    if choice == 2:
        lists()
    if choice == 3:
        buySell()
    if choice == 4:
        timeJumping()
    choice = menu()