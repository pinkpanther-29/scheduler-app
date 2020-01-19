import json

def roundup(time):
    min = time % 100
    hour = int(time/100)
    if min >= 45:
        hour = hour + 1
        min = 0
    elif min >= 15:
        min = 30
    else:
        min = 0
    return min+(hour*100)

def rounddown(time):
    min = time % 100
    hour = int(time/100)
    if min >= 45:
        hour = hour + 1
        min = 0
    elif min >= 15:
        min = 30
    else:
        min = 0
    return min+(hour*100)

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
        startTime = int(currentString[0:2]) * 100 + int(currentString[3:5])
        startTime = rounddown(startTime)
        endTime = int(currentString[6:8]) * 100 + int(currentString[9:11])
        endTime = roundup(endTime)
        scheduleOfWeek[i].append([startTime, endTime])
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