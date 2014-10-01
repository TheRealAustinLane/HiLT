import csv as csv

f = open('input.txt', 'r+')
spamreader = csv.reader(f, delimiter='(')

with open('output.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for line in spamreader:
        spamwriter.writerow(line)
