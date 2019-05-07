#! Python3
# This will take 

import csv

with open("c:\\scripts\\Yr11_Email_Addresses.csv","r") as data, \
open("c:\\scripts\\usernames.csv", "w", newline ='') as outfile:

    reader = csv.reader(data)
    header = next(reader) # The first line is a header
    writer = csv.writer(outfile)
    for row in reader:
        email = [(row[1])]
        for item in email:
            username = [item.split('@')[0]]
            writer.writerow(username)
    outfile.close()
