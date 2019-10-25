"""
Program prints out menu options and takes an input from user.
Based on the user input program calculates the statistics for
temperature sensors and output the results to user. The input file
is file.csv
"""

import os
import math

def recurciveSort(list_to_sort, key=0):
    for i in range(0, len(list_to_sort) - 1):
        if list_to_sort[i][key] > list_to_sort[i + 1][key]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            recurciveSort(list_to_sort, key)
            break
    return list_to_sort

def menue():
    """
    prints menu option to the screen
    """
    menu_string = "\n Main Menu\n" \
                  "---------\n" \
                  "1 - Process a new data file\n" \
                  "2 - Choose units\n" \
                  "3 - Edit room filter\n" \
                  "4 - Show summary statistics\n" \
                  "5 - Show temperature by date and time\n" \
                  "6 - Show histogram of temperatures\n" \
                  "7 - Quit"

    print(menu_string)

def newFile(processfile):
    """
    function opens new file
    :return:
    """
    newfilein = input("Please enter the filename of the new dataset: ")
    if os.path.isfile(newfilein):
        processfile.processFile(newfilein) #calling class
        print("Total number of samples loaded is ", processfile.getLoadedTemps())
        while True:
            name = processfile.setName(input("Please provide a 3 to 20 character name for the dataset: "))
            if name:
                break
            else:
                print("The data set name provided is invalid. Try again.")
                continue
        return processfile
    print(newfilein + " not found!")
    return

def printFilter(sensor_list, filter_list):
    """
    function takes sorted_list and filter_list as parameters
    and output ACTIVE on not ACTIVE results based on value in
    filter_list
    :param list1:
    :param list2:
    :return:
    """
    for i in range(0, len(sensor_list)):
        a, b, c = (sensor_list[i])
        if c in filter_list:
            print(a + ': ', b + ' ACTIVE')
        else:
            print(a + ': ', b)

def chooseUnits(units):
    """
    function that process units
    :param unit:

    """
    global current_unit
    while (True):
        #print("Default Unit is in ", units[0][0], "and will be represented by letter", units[0][1])
        print("Current unit is ", units[current_unit][1])
        for k, v in units.items():
            print(k, '-', v[0])
        try:
            unit_choose = int(input("Choose new units: "))
            if unit_choose in (list(units.keys())):
                print("Your unit choice is", units[unit_choose][0])
                break

        except ValueError:
            print("Your unit choice is invalid. Select from " , list(units.keys()))
            return units[0][1]
            continue

    return unit_choose


def changeFilter(sensors, sensor_list, filter_list):
    """
    function takes sensor dictionary, sorted_list and filter list as parameters
    function deletes or appends filter_list based on user sensor selection
    :param sensors:
    :param sensor_list:
    :param filter_list:
    :return:
    """
    print("You chose to Change Filters. \n")
    while True:
        printFilter(sensor_list, filter_list)
        selection = (input("\nType the sensor number to toggle (e.g 4201) or x to exit: "))
        if selection == 'x':
            break
        elif selection not in (list(sensors.keys())):
            print("Invalid selection, must be in ", list(sensors.keys()), "\n")
            continue
        else:
            sensor_number = sensors[selection][1]
            print("\nThe following sensor number will be updated: ", sensor_number, "\n")
            if sensor_number in filter_list:
                filter_list.remove(sensor_number)
            else:
                filter_list.append(sensor_number)

def printSummaryStatstics(dataset, filter_list):
    """
    function prints summary statistics
    """
    global current_unit
    global units

    stats = dataset.getSummaryStatistics(filter_list)
    #print(mint, maxt, average)
    # if mint != 0 and maxt != 0 and average != 0 :
    if stats is None:
        print("Please load data file and make sure at least one sensor is active")
    else:
        print("Minimum Temperature:","{0:.2f}".format(convertUnits(stats[0], current_unit)), units[current_unit][1])
        print("Maximum Temperature:","{0:.2f}".format(convertUnits(stats[1], current_unit)), units[current_unit][1])
        print("Average Temperature:",  "{0:.2f}".format(convertUnits(stats[2], current_unit)), units[current_unit][1])



def printTempByDayTime(dataset, filter_list):
    if dataset.getLoadedTemps() is None:
        print("Please load data file")
        return
    print("Average Temperatures for", dataset.getName())
    print("Units are in", units[current_unit][0])
    #print('             ', end='')
    [print("{:6}".format(DAYS[day]), end='') for day in range(0, 7)]
    print()
    for hour in range(0, 24):
        print(HOURS[hour], end=' ')
        for day in range(0, 7):
            target = dataset.getAvgTemperatureDayTime(filter_list, day, hour)
            if target is None:
                print("   ---", end='');
            else:
                print("{0:6.1f}".format(convertUnits(target, current_unit)), end='')
        print()





def printHistogram():
    """
    function print histogram
    """
    pass

def convertUnits(celsius_value, units=0):
    """
    function takes parameters and units and converts the temperature into other units
    :param celsius_value:
    :param units:
    :return:
    """
    if (units == 0):
        return celsius_value

    elif (units == 1):
        fahrenheit_value = (celsius_value * 9.0 / 5.0) + 32
        return fahrenheit_value

    elif (units == 2):
        kelvin_value = celsius_value + 273
        return kelvin_value

class TempDataset():
    """
    class process the set of temperature datasets
    """
    # class ("static") intended constants
    MINLENGTH = 3
    MAXLENGTH = 20

    # class attributes that will change over time
    number_of_dataset_objects = 0
    total_samples_loaded = 0

    # initializer ("constructor") method -------------------------------
    def __init__(self, filename=None):
        # class-defined instance attributes (attributes)
        self.filename = filename
        self.data_set = []
        self.name_of_dataset = "Unnamed"
        TempDataset.number_of_dataset_objects += 1

        # repair mutable defaults

        # mutator ("set") methods -------------------------------

    def setName(self, name_of_dataset):
        """
        function checks if name_of_dataset meets the requirements
        :param name_of_dataset:
        :return:
        """
        if TempDataset.MINLENGTH <= len(name_of_dataset) <= TempDataset.MAXLENGTH:
            self.name_of_dataset = name_of_dataset
            return True
        # else
        return False

    def processFile(self, filename):
        """
        function process the file
        :return:
        """
        try:
            my_file = open(filename, 'r')
        except FileNotFoundError:
            # print("File not found.  Program aborted.")
            return False
        for next_line in my_file:
            # my_tuple = tuple(next_line.split(","))
            day, time, sensor, readtype, temp = next_line.split(",")
            if readtype == 'TEMP':
                TempDataset.total_samples_loaded += self.getLoadedTemps()
                self.data_set.append((int(day), math.floor(float(time) * 24),
                                      int(sensor), float(temp)))
        # print (self.data_set)
        # print (TempDataset.total_samples_loaded)
        return TempDataset.total_samples_loaded

    # accessors -----------------------------------------------
    def getName(self):
        """
        takes no arguments, returns the name of our data
        :return:
        """
        return self.name_of_dataset

    def getSummaryStatistics(self, filter_list):
        """
        :param filter_test:
        :return:
        """
        if self.data_set is None:
            return None

        temps = [elem[3] for elem in self.data_set if elem[2] in filter_list]
        if len(temps) == 0:
            return None
        else:
            return (min(temps), max(temps), sum(temps) / len(temps))


    def getAvgTemperatureDayTime(self, filter_list, day, time):
        '''
        :param filter_list:
        :param day:
        :param time:
        :return:
        '''
        if self.data_set is None:
            return None

        total = 0
        temp_at_time_day = [i for i in self.data_set if i[0] == day and i[1] == time and i[2] in filter_list]
        for i in temp_at_time_day:
            total += i[3]
        if total != 0 and temp_at_time_day != 0 :
            averaget = total/len(temp_at_time_day)
            #print("Average test:", total/len(temp_at_time_day))
            #return self.data_set
            return convertUnits(averaget, current_unit)
        else:
            #print("Cant calculate average test, all sensors are inactive.")
            return None

    def getNumTemps(self, filter_list, lower_bound, upper_bound):
        """
        :param filter_list:
        :param lower_bount:
        :param upper_bound:
        :return:
        """
        if self.data_set is None:
            return None
        return 0

    def getLoadedTemps(self):
        """
        :return:
        """
        if self.data_set is None:
            return None
        return len(self.data_set)

    # class accessors ----------------------------
    @classmethod
    def getNumObjects(cls):
        """
        Returns the number of objects that have been created
        """
        return cls.number_of_dataset_objects

    @classmethod
    def getTotalSamples(cls):
        """
        Takes no arguments,
        Returns the number of samples that have been loaded
        across all objects
        """
        return cls.total_samples_loaded

# def main():

print("\nSTEM Center Temperature Project\n" \
          "Victoria Vyedina\n")

sensors = {
        "4213": ('STEAM CENTER', 0),
        "4201": ('Foundation lab', 1),
        "4204": ('CS Lab', 2),
        "4218": ('Workshop Room', 3),
        "4205": ('Tiled Room', 4),
        'Out': ('Outside', 5)

    }

units = {
        0: ("Celsius", "C"),
        1: ("Fahrenheit", "F"),
        2: ("Kelvin", "K")
    }

DAYS = {
    0 : "SUN",
    1 : "MON",
    2 : "TUE",
    3 : "WED",
    4 : "THU",
    5 : "FRI",
    6 : "SAT"
}

HOURS = {
    0 : "Mid-1AM ",
    1 : "1AM-2AM ",
    2 : "2AM-3AM ",
    3 : "3AM-4AM ",
    4 : "4AM-5AM ",
    5 : "5AM-6AM ",
    6 : "6AM-7AM ",
    7 : "7AM-8AM ",
    8 : "8AM-9AM ",
    9 : "9AM-10AM ",
    10 : "10AM-11AM",
    11 : "11AM-NOON",
    12 : "NOON-1PM ",
    13 : "1PM-2PM ",
    14 : "2PM-3PM ",
    15 : "3PM-4PM ",
    16 : "4PM-5PM ",
    17 : "5PM-6PM ",
    18 : "6PM-7PM ",
    19 : "7PM-8PM ",
    20 : "8PM-9PM ",
    21 : "9PM-10PM ",
    22 : "10PM-11PM",
    23 : "11PM-MID ",
}


current_unit = 0
current_set = TempDataset()

sensor_list = [(k, v[0], v[1]) for k, v in sensors.items()]
filter_list = [(i[1][1]) for i in sensors.items()]

# print(filter_list)
# print(recurciveSort(sensor_list, 0))
recurciveSort(sensor_list, 0)
# printFilter(sensor_list, filter_list)

while True:
    menue()
    current_set.getAvgTemperatureDayTime(filter_list, 5, 7)
    try:
        selection = int(input("\nWhat is your choice? "))
    except ValueError:
        print("Invalid Selection, should be integer!")
        continue
    if selection == 7:
        break
    elif selection < 1 or selection > 7:
        print("Invalid selection, should be between 1 and 7!")
    else:

        if selection == 1:
            newFile(current_set)
            # try:
            #     if current_set.data_set:
            #         print("Testing Curent Data Set for menue item #1.")
            #         print([current_set.data_set[k] for k in range(0, 5000, 1000)])
            #     else:
            #         print("not set")
            # except (TypeError, AttributeError):
            #     pass

        elif selection == 2:
            print("\nYour temperature unit for menu item #2 is ", selection)
            current_unit = chooseUnits(units)
            # print("Unit conversion selection is ", current_unit)
            # print("Testing Temperature Convertion Unit....")
            # conv_result = convertUnits(25,current_unit)
            # print("The temperature in ", units[current_unit][0], "is ", conv_result,  units[current_unit][1])

        elif selection == 3:
            changeFilter(sensors, sensor_list, filter_list)
        elif selection == 4:
            #printSummaryStatstics(current_set, filter_list, current_unit, units)
            printSummaryStatstics(current_set, filter_list)
            current_set.getSummaryStatistics(filter_list)
            #current_set.getAvgTemperatureDayTime(filter_list, 5, 7)
            # print("cs", current_set.getAvgTemperatureDayTime(filter_list, 5, 7))
        elif selection == 5:
            printTempByDayTime(current_set, filter_list)

        elif selection == 6:
            printHistogram()


