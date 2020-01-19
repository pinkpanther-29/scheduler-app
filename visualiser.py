import json

f = open("schedules.json", "r")
content = json.load(f) #need json.load!

bins = [] # this is initialising a list of zeroes!
for i in range(0,12):
    bins.append(0)

list = {"Time = 9-9:30"}

print(bins)