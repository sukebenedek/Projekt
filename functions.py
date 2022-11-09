from classs import Result

results = []

f = open('ecdl.csv', 'r', encoding='UTF=8')
f.readline()
for row in f:
    r = Result(row.strip())
    results.append(r)
f.close()


# for i in results:
#     print(i.name, i.percent)

print(results[0].name)
