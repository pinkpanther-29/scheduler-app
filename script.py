import json

try:
    f = open("schedules.json", "r")
    storedSchedule = json.load(f) # to convert it into an object, instead of a string
    print(storedSchedule)
    print(type(storedSchedule))
    f.close()
except:
    print("File not accessible. Making new file.")
    storedSchedule = []

myfile = open("schedules.json","w")

daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

scheduleOfWeek = [[], [], [], [], []]

for i in range(0,5):
    userIn = input("Enter your " + daysOfWeek[i] + " unavailability, as (hh.mm-hh.mm,hh.mm-hh.mm...) in military time: ") # plus sign to add strings concatenation

    while len(userIn) > 0:
        currentString = userIn[0:11]
        scheduleOfWeek[i].append([int(currentString[0:2]) * 100 + int(currentString[3:5]) , int(currentString[6:8]) * 100 + int(currentString[9:11])])
        userIn = userIn[12:len(userIn)]

print(scheduleOfWeek)
storedSchedule.append(scheduleOfWeek)
myfile.seek(0)
myfile.write(json.dumps(storedSchedule, indent=2))

"""        scheduleOfWeek[
            [
                [hhmm,hhmm],[hhmm,hhmm]
            ]
            [
                [hhmm,hhmm]
            ]
        ]
        scheduleOfWeek[0][] """