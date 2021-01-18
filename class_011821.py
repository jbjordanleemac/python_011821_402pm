#!/usr/bin/python

import mymodule_011821
import json


class longweekend():
  extra_day="Yes extra day off"
  extra_break="Yes extra day break"

  def __init__(self, whichday, dowhat):
    self.whichday=whichday
    self.dowhat=dowhat

  def location(self, where):
    print('During longweekend it is a good idea to plan ' + self.dowhat + ' at ' + where + ' on ' + self.whichday + ' which is always relax and pleasant ')

l1=longweekend('Sat', 'Hiking')
print(l1.whichday)

l1.location('Lake Chabot')

day='Mon'

# if else statement

if day == "Mon":
  print('Today is Mon')
else:
  print('Today is NOT Mon')

# try except

year=2021

try:
  print(years)
except:
  print('years is not defined')

# define dictionary

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

# for loop

for a in thisdict:
  print(a)

# adding key value on dict

thisdict["Thurs"]="Four"

for b in thisdict:
  print(b)

# changing value on dict and print value on dict

thisdict["Thurs"]="Fourr"

for c in thisdict:
  print(thisdict[c])

# how to define a list

thatlist=["Jan", "Feb", "March"]

for d in thatlist:
  print(d)

# how to add two list together

e=["one", "two", "three"]
f=["four", "five", "six"]

for g in f:
  e.append(g)

for h in e:
  print(h)

# while loop

grade=7

print('Attenting grade ' + str(grade) + ' Now')

while grade < 12:
  grade+=1
  print('Will attend grade ' + str(grade) + ' next')

print('Congras, Go to college next ')

# import module and run method

mymodule_011821.greeting('Jordan')

# json

thisjson='{"one":"mon", "two":"tue", "three":"wed"}'

i=json.loads(thisjson)

print(i["one"])

print(i["two"])
