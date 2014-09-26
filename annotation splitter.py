import csv
import re

f = open('test.txt', 'wb')
try:
    spamwriter = csv.writer(f)
    spamwriter.writerow(('Number', 'String'))
    

input('press 1')
input('press b')
