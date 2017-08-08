import csv
with open("norvig-list.txt") as nl:
    counter = 0
    for x in nl:
        m = x.strip().split("\t")
        print(m)
        counter += 1
        if counter==10:
            break


