import csv

with open("data.csv") as file:
    read = csv.reader(file)
    # print(list(read))
    for rows in read: 
        print(rows)