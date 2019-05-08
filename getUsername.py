#! Python3
# Take a list of email addresses exported from Active Directory, extract the username, and write them to file

import csv

# Open csv file, and create new csv for writing to

with open("c:\\scripts\\Yr11_Email_Addresses.csv","r") as data, \
open("c:\\scripts\\test.csv", "w", newline ='') as outfile: 

    reader = csv.reader(data)
    header = next(reader) # The first line is a header
    writer = csv.writer(outfile)
    writer.writerow(['username, password, name, email']) #write header row to file
    for row in reader:
        name = [(row[0])]
        email = [(row[1])] # email is second column in csv file
        firstname = (name[0].split(', ')[1].title()) # split full name column into first name and last name
        lastname = (name[0].split(', ')[0].title())
#        print ((firstname + ' ' + lastname))
        for item in email:
            username = [item.split('@')[0]] # split the email address at '@' and keep the first section 
            writer.writerow(username)       # write extracted username to csv file
    print("Writing usernames to file " + str(outfile).split(' ')[1][6:])

# TODO  learn how to write both usernames and full name fields to CSV file
