import csv as csv

f = open('test.csv', 'r+')
spamreader = csv.reader(f, delimiter=' ')
for line in spamreader:
    print line
