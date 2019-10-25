 # Topics: Arithmetic, Data Types, User Input,
 # Formatting Output, Importing Modules
 # Description: take user input, verify it and use it in calculations
 # User Input: name and student ID
 # Output: expression results as per lab spec.
 # Development Environment:  MAC home


import datetime

def intro():
    print ("\nThis program requires you to input  name and  Id \n"
           "The  name should be from 2 to 15 characters long and include\n"
           "only letters. The  Id must be integer and exactly 8 charcters long.\n")

# setting up defaults to protect the application from unwanted client inputs


class UserInfo():
    # setting class variables
    MINLN = 2
    MAXLN = 15
    IDLEN = 8

    # class attributes that might change
    default_student_lastname = "X"
    default_student_id = "X"
    #initializing the constructor

    def __init__(self, student_lastname=None, student_id=None):
        self.student_lastname = student_lastname if student_lastname is not None else self.default_student_lastname
        self.student_id = student_id if student_id is not None else self.default_student_id

    #mutators
    def  set_last(self, student_lastname):
        if not(self.MINLN <= len(student_lastname) <= self.MAXLN)\
                or not student_lastname.isalpha():
            return False
        self.student_lastname = student_lastname

    def set_id(self, student_id):
        if student_id:
            try:
                if int(student_id):
                    self.student_id = student_id
                else:
                    self.student_id = self.default_student_id
            except ValueError:
                self.student_id = self.default_student_id
            return
        else:
            self.student_id = student_id

    #accessors

    def get_name(self):
        return self.student_lastname

    def get_id(self):
        if self.student_id is None or len(student_id) != self.IDLEN:
            return self.default_student_id
        else:
            return self.student_id

#instantiating the datetime object
today_date = datetime.datetime.now()

#printing out the introduction
intro()
#print (str(today_date))
print ("Current date and time using strftime:",today_date.strftime("%Y-%m-%d %H:%M"))
#print ("Current date and time using isoformat: ", today_date.isoformat())
print ("Today's date: {}/{}/{}".format(today_date.month, today_date.day, today_date.year), "\n")

while True:
    myinfo = UserInfo()
    lastname = input("Enter your Last Name: ")
    student_id = input("Enter your Student Id: ")
    myinfo.set_last(lastname)
    myinfo.set_id(student_id)
    sname = myinfo.get_name()
    sid = myinfo.get_id()
    print(sname,sid)
    if sname == 'X' or sid == 'X':
        print("Invalid Last Name or Studentid.\n")
        continue
    else:
        #calculate the sum of integers in my student id
        my_id = sum(int(x) for x in str(sid))
        #calculate sum of integers (2 + 3 + 4 ... +len(lastname)
        sums = sum(int(i) for i in range(2, len(lastname)+1))
        commands = [my_id,
                    len(lastname),
                    my_id/2,
                    my_id % 2,
                    sums,
                    my_id + len(lastname),
                    abs(len(lastname) - my_id),
                    my_id / (len(lastname) + 1100),
                    ((len(lastname) % len(lastname)) and (my_id * my_id)),
                    (1 or (my_id / 0)),
                    round(3.15, 1)]

        print(("Family Name entered: {}").format(myinfo.get_name()))
        print(("Student Id entered: {}").format(myinfo.get_id()))

        break

for i in range(0, len(commands)):
    if i == 0:
        print("my_id: ", commands[i])
    elif i == 1:
        print("n_let: ", commands[i])
    else:
        print("expression"+str(i - 1), commands[i])




 

