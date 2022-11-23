import os

today = "2022-10-23"
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

    os.system("cls")
    print(f"Jelenlegi dátum: {date}\n")
    input("Ok")

    