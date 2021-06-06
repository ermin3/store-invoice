import csv
with open('py.csv', newline='')as pr:
    read = csv.reader(pr, delimiter=',', quotechar='"')
    print('unos racuna \n---------')
    for i in read:
        x=i[1]
    print(x)
