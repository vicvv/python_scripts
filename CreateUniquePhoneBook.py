####################################################################
# Description: Write a program that counts the number of entries in a phonebook file.
# Print out a result message and number of entries in a phonebook for
# a valid address text file. Create a second file, phonebook.txt,
# with unique records tht have name and phone number
# Version 1
# Development Environment:  MAC, Home
#
# ###################################################################
introduction = '''
Program takes file name as an input form user,counts the number 
of entries in a phonebook file  and prints out a result message and number of entries 
in a phonebook for a valid address text file. Also it creates a second file, phonebook.txt, 
where the records created have the following format:

Foothill, Ann
650-949-7259
De Anza, Bob
408-864-8877

'''
RECNUM = 5
RECLNUM = 0
RECFNUM = 1
RECPHONE = 4
# introduction details what this program does
print(introduction)

# filemanip takes list as a parameter after user input is sanitised in while loop
def filemanip(composite_list):
    d = {}
    # getting records into separate lists
    # below dictionary is to make sure that we do not have a duplicate records
    for item in composite_list:
        d[item[RECLNUM] + ' ' + item[RECFNUM]] = item[RECPHONE]
    return d

# getting input from the users. Making sure that each record has 5 lines
dict = {}
while True:
    file = input("Enter the file name (Hit <Enter> to quit): ")
    # checking if we can open the input file addresbook.txt
    if file == '':
        break
    else:
        try:
            with open (file, 'r') as fr:
                line = [line.strip() for line in fr]
        except IOError as e:
            print(e , '\n')
            continue
        # checking if the input file has correct format for us to process
        if len(line) % RECNUM == 0:
            print("Total lines in the file: ", len(line))
            print("Total Address Records in the file: ", int(len(line) / RECNUM))
            composite_list = [line[x:x + RECNUM] for x in range(0, len(line), RECNUM)]
            # calling filemanip() function that will parse the list and return dictionary
            # since there are multiple files I will update the dictionary which I am going
            # to use as an input in the phonebook.txt file
            dict.update(filemanip(composite_list))
        else:
            print("The supplied file has incorrect format.\n")

# finally creating the phonebook.txt file with unique records
try:
    with open("phonebook.txt", 'w') as fo:
        for k, v in dict.items():
            fo.write(k + '\n' + v + '\n')
            #print(k, v)
except IOError as e:
        print(e)

'''

Program takes file name as an input form user,counts the number 
of entries in a phonebook file  and prints out a result message and number of entries 
in a phonebook for a valid address text file. Also it creates a second file, phonebook.txt, 
where the records created have the following format:

Foothill, Ann
650-949-7259
De Anza, Bob
408-864-8877


Enter the file name (Hit <Enter> to quit): err.txt
The supplied file has incorrect format.

Enter the file name (Hit <Enter> to quit): somefile.txt
[Errno 2] No such file or directory: 'somefile.txt' 

Enter the file name (Hit <Enter> to quit): addressbook.txt
Total lines in the file:  30
Total Address Records in the file:  6
Enter the file name (Hit <Enter> to quit): demo.txt
Total lines in the file:  10
Total Address Records in the file:  2
Enter the file name (Hit <Enter> to quit): demoother.txt
Total lines in the file:  20
Total Address Records in the file:  4
Enter the file name (Hit <Enter> to quit): 

Process finished with exit code 0


'''

