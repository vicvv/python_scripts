#
# Topics: Python WWW API. Application: Web and Search
# Formatting Output, Importing Modules
# Description: See details below
# User Input: URL
# Output: results as per  spec.
# Development Environment:  MAC home
#
# Understand the Application
#
# The National Academy of Science (NAS) marketing department is interested to get an accurate assessment on the coverage
# of publicized topics on the current website. The marketing strategy team is divided over which of a list of topics is
# most widely represented on the website.
# You have been hired to put a decision on the business operations (bizops) table as to which topic is most represented
# on the NAS website.
# Specifically we will write a Python3 program that takes the URL of the National Academy of Science and a list of topics.
# For each topic of interest, your solution intelligence will compute the number of instances of each topic on the
# NAS website providing a simple yet complete report.
#
# The Program Spec
#
# -Write a program that takes the NAS website url:  http://www.nasonline.org,Links to an external site. downloads the HTML
# document, and decodes it into a string.
#
# -Create a list of the topics under review which include:  research, climate, evolution, cultural and leadership.
# To provide additional insight to the bizops team, include an additional topic of your selection to the review list.
#
# -Determine the number of occurrences of each topic that appears on the webpage.
#
# -Provide a report summary that specifies the topic of interest and the number of times that the subject presents on
# the NAS website.
#
# Import the datetime Links to an external site.module to generate the date of your report run. Print this date in
# your run output.
#
# Test Run Requirements:
#
# 1.Topic list contains the list of subjects in the program spec (including a minimum of one additional insight
# subject presented by you i.e. a minimum of 6 topics).
# 2.The urlopen() response usually returns a special object called a byte string. In order to work with the
# response as a string, use the decode() method to convert it into a string with an encoding.  Use 'utf-8' encoding.
# 3.Validate if there is an error opening the url or decoding it.
# 4.Generate a report summary that pairs the subject with the number of occurrences as measured by number of
# instances found of the topic on the website.
#
#

import urllib.request
import urllib.parse
import re
import datetime

# creating class to parse the url
class ProcessUrl:
    values = {'s':'basic', 'submit':'search'}
    RESULT = {}
    RESULTS = {}

    def __init__(self,url):
        self.url = url
        self.data = urllib.parse.urlencode('')
        self.data = self.data.encode('utf-8')
        self.req = urllib.request.Request(self.url, self.data)
        self.resp = urllib.request.urlopen(self.req)
        self.respData = self.resp.read()

    def set_url(self):
        if url is not None:
            self.url = url
            return self.url
        else:
            return False


    def procesparams(self, *params):
        self.RESULTS = {}
        for self.param in params:
            i = re.findall(self.param, str(self.respData).lower(), re.IGNORECASE | re.DOTALL)
            if i:
                self.RESULT = {x:i.count(x) for x in i}
                self.RESULTS.update(self.RESULT)
            else:
                self.RESULTS[self.param] = 0
        return self.RESULTS


url = 'http://www.nasonline.org/'
tryme = ProcessUrl(url)
results = tryme.procesparams('research', 'membership', 'climate', 'evolution', 'leadership',
                             'promotes outstanding science','Policy Studies & Reports')

print("\nToday's date is ", datetime.date.today(), "\n")
for key, values in results.items():
    print("Term '"+ key.title()+"'","appears ", values, "time(s) in " + url)
while True:
    userchoice = input("\nInput term or terms to search in http://www.nasonline.org: ")
    if not userchoice:
        break
    else:
        uch = ProcessUrl(url)
        result = uch.procesparams(userchoice)
        for key, values in result.items():
            print(key, "appears ", values, "time(s);")


