today = "2022-10-23"

# print("Today's date:", today)
today = today.split("-")

# print(today)

# print()
day = int(today[2])
month = int(today[1])
year = int(today[0])

def jumpDate(howMuch):
    global day, month, year
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

    return(f"{year}-{month}-{day}")



# def jumpDate(howMuch):
#     count = 0
#     
#         today[2] = int(today[2]) + 1
        
#         if int(today[2]) + 1 > 31:
#             for i in today: #ugorjon hónapot, napot 0-za
#                 count += 1
#                 if count == len(today):
#                     print(f'{i}', end="\n")
#                 else:
#                     print(f'{i}', end="-")
#         else:
#             count = 0
#             for i in today:
#                 count += 1
#                 if count == len(today):
#                     print(f'{i}', end="\n")
#                 else:
#                     print(f'{i}', end="-")
#     if howMuch == "month":
#         today[1] = int(today[1]) + 1
#         for i in today:
#             count += 1
#             if count == len(today):
#                 print(f'{i}', end="\n")
#             else:
#                 print(f'{i}', end="-")

        
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))
# print(jumpDate("month"))

