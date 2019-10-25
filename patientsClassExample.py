class Patient:
    # class ("static") intended constants
    ORIGINAL_DEFAULT_NAME = "(no name)"
    ORIGINAL_DEFAULT_ID = 0
    ORIGINAL_DEFAULT_TEMPERATURE = 98.6

    MIN_STRING_LENGTH = 2
    MAX_STRING_LENGTH = 40
    MIN_ID = 0
    MAX_ID = 9999
    MIN_TEMP = 88
    MAX_TEMP = 111
    ALARM_TEMP = 103.5


    # class attributes that will change over time
    default_name = ORIGINAL_DEFAULT_NAME
    default_id = ORIGINAL_DEFAULT_ID
    default_temperature = ORIGINAL_DEFAULT_TEMPERATURE

    # initializer ("constructor") method -------------------------------
    def __init__(self,
                 name=None,
                 id=None,
                 temperature=None):
        # repair mutable defaults
        if (name is None):
            name = self.default_name
        if (temperature is None):
            temperature = self.default_temperature
        if (id is None):
            id = self.default_id

        # instance attributes
        if (not self.set_name(name)):
            self.name = self.default_name
        if (not self.set_id(id)):
            self.id = self.default_id
        if (not self.set_temperature(temperature)):
            self.temperature = self.default_temperature


    #mutators
    def set_name(self, name):
        if not self.valid_string(name): # placeholder for real test
            return False
        # else
        self.name = name
        return True

    def set_id(self, id):
        if not self.valid_id(id):  # placeholder for real test
            return False
        # else
        self.id = id
        return True

    def set_temperature(self, temperature):
        if not self.valid_temp(temperature): # placeholder for real test
            return False
        # else
        self.temperature = temperature
        return True

    # accessors -----------------------------------------------

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_temperature(self):
        return self.temperature

    # output method  ----------------------------------------

    def display(self,
                client_intro_str="--- PATIENT DATA ---"):
        print(self.to_string(client_intro_str))

    # instance helpers -------------------------------

    def to_string(self, optional_title=" ---------- "):
        if not True:  # placeholder for real test
            optional_title = " ---------- "
        ret_str = ((optional_title + " name: {}"  + " id: {}" + " temp: {}(F).").
                       format(self.name, self.id, self.temperature))
        if (self.temperature >= self.ALARM_TEMP):
            ret_str += "\n     *** urgent: attend immediately ***"
        return ret_str

    # static and class helpers -------------------------------

    @classmethod
    def valid_string (cls, string_to_test):
        if type(string_to_test) != str or not (cls.MIN_STRING_LENGTH <= len(string_to_test) <= cls.MAX_STRING_LENGTH):
            return False
        return True

    @classmethod
    def valid_id(cls, id_to_test):
        if type(id_to_test) != int or not (cls.MIN_ID <= id_to_test <= cls.MAX_ID):
            return False
        return True

    @classmethod
    def valid_temp(cls, temp_to_test):
        if (type(temp_to_test) != int and type(temp_to_test) != float) or not (cls.MIN_TEMP <= temp_to_test <= cls.MAX_TEMP):
            return False
        return True


    # class mutators and accessors ----------------------------

    @classmethod
    def set_defalut_id(cls, new_defalut_id):
        if not cls.valid_id(new_defalut_id):
            return False
        cls.default_id = new_defalut_id

    @classmethod
    def set_defalut_name(cls, new_default_name):
        if not cls.valid_string(new_default_name):
            return False
        cls.default_name = new_default_name

    @classmethod
    def set_defalut_temperature(cls, new_default_temperature):
        if not cls.valid_temp(new_default_temperature):
            return False
        cls.default_temperature = new_default_temperature
        return True

    @classmethod
    def get_default_id(cls):
        return cls.default_id

    @classmethod
    def get_default_name(cls):
        return cls.default_name

    @classmethod
    def get_default_temperature(cls):
        return cls.default_temperature





# client --------------------------------------------

# # instantiate two Patients
# person1 = Patient()
# person2 = Patient()
# person3 = Patient("Racha", 32, 99.9)
# person4 = Patient("ill patient", 555, 103.9)
#
# # display both
# person1.display("patient 1")
# person2.display("patient2")
# person3.display("patient3")
# person4.display("patient 4")
#
# person1.set_name("Fred")
# person1.set_id(1234)
# person1.set_temperature(103.7)
#
# person2.set_name("Janis")
# person2.set_id(5555)
# person2.set_temperature(103.7)
#
# # display both
# person1.display("patient 1")
# person2.display("patient2")
# person3.display("patient3")
# person4.display("patient 4")
#
#
# print("\nMore tests ----------- :\n")
# # test a couple mutators for data filtering
# if (not person1.set_temperature(333)):
#     print("Unable to set temperature to 333.")
# else:
#     print("Temp set to 333.")
#
# if (not person2.set_id(-44)):
#     print("Unable to set ID to -44.")
# else:
#     print("ID set to -44.")
# print()
#
# # test a few accessors
# print("Patient #1's name is " + person1.get_name())
# print ("The minimum valid temperature is " + str(Patient.MIN_TEMP))


#main

def get_patient_id():
    string_in = input("What's the patient id: ")
    id = int(string_in)
    return id

def get_patient_name():
    string_in = input("What is the patient name: ")
    return string_in

def get_patient_temp():
    string_in = input("what is temperature: ")
    temperature = float(string_in)
    return temperature

#client

person1 = Patient()
person2 = Patient()

print("Patient #1 data")
user_id = get_patient_id()
user_name = get_patient_name()
user_temp = get_patient_temp()

# set patient #1
if (not person1.set_name(user_name)):
    print("Error in patient name: Invalid length.")
if (not person1.set_id(user_id)):
    print("Error in patient id: not int or out-of-range.")
if (not person1.set_temperature(user_temp)):
    print("Error in patient temperature: not float or out-of-range.")

# get the info for patient #2:
print("\nPatient #2 ---")
user_id = get_patient_id()
user_name = get_patient_name()
user_temp = get_patient_temp()

# set patient #2
if (not person2.set_name(user_name)):
    print("Error in patient name: Invalid length.")
if (not person2.set_id(user_id)):
    print("Error in patient id: not int or out-of-range.")
if (not person2.set_temperature(user_temp)):
    print("Error in patient temperature: not float or out-of-range.")

# find the more urgent patient
if person1.get_temperature() > person2.get_temperature():
    first = person1
    second = person2
else:
    first = person2
    second = person1

# display results
first.display("Patient with higher temperature:")
second.display("Patient with lower temperature:")



