#!/usr/bin/python

import sys
import mymodule_012021
import json

from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f", "--file", action="store", type="string", dest="file", help="<file>")
(options, args)=parser.parse_args()

if options.file == None:
  sys.exit( 1 )
else:
  file == options.file

l=open(str(options.file), 'ro')
print(l.read())


class longweekend():
  extra_time_off='Yes extra time off'
  learn_more_stuff='Yes learn more stuff'

  def __init__(self, whichday, dowhat):
    self.whichday=whichday
    self.dowhat=dowhat

  def location(self, where):
    print('Going for ' + self.dowhat + ' at ' + where + ' during ' + self.whichday + ' on long weekend always pleasant ') 

l1=longweekend('Sat', 'Hiking')

print(l1.whichday)

l1.location('Lake Chabot')

class longweekend2(longweekend):
  pass

l2=longweekend2('Sun', 'Church')

print(l2.dowhat)

l2.location('Home')

# run method from imported module

mymodule_012021.greeting('Jordan')

# define dict

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

# print key from dict

for a in thisdict:
  print(a)

# print value from dict

for b in thisdict:
  print(thisdict[b])

# adding key value in dict

thisdict["Thurs"]="Four"

for c in thisdict:
  print(thisdict[c])

# define a list

thatlist=["mon", "tue", "wed"]

# print list

for d in thatlist:
  print(d)

# how to append two lists together

e=["one", "two", "three"]
f=["four", "five", "six"]

for g in f:
  e.append(g)

for h in e:
  print(h)

# json format

i='{"mon":"one", "tue":"two", "wed":"three"}'
j=json.loads(i)

print(j["tue"])

# while loop

grade=7

print('You are curretly attending grade ' +str(grade) + ' Now ')

while grade < 12:
  grade+=1
  print('You will be attending grade ' + str(grade) + ' next ')

print('Congrats, you ready for college next')

# try except statement

today='Wed'

try:
  print(todayy)
except:
  print('todayy is NOT defined')

# how to read a file and print the line one by one

k=open('testfile', 'ro')

print(k.read())

# if else statement

today="Wed"

if today == "Wed":
  print('Today is Wed')
else: 
  print('Today is NOT Wed')

# method return value

def result(num):
  return num * 4

print(result(5))

# format 1

name="Jordan Lee"

print('Your name is ' + name)

print('Your Full name is %s' % name)
