"""
RANDO: Fang Chen, Julia Lee
Soft Dev, pd 2
K06 - Divine your Destiny!
2022-10-03
time spent: 1 hr

DISCO:
    After setting a variable in the file to a value, calling a defined function (which changes the value of the variable of the same name) 
    does not overwrite the value of said variable set outside the function. (Only tested with ints)

    Example: 
        x = 1
        def change():
            x = 2
        change()
        print(x)    # Output = 1

QCC:
    How can we update the value of an initialized variable by calling a function?

HOW THIS SCRIPT WORKS:
    00. Convert data from csv file to a dictionary {rollover percentage : occupation name} by splitting
    01. Select a random int from 1 to 998 (with randint, so both end values are inclusive) and divide by 10.0 to get a float [1.0, 99.8]
    02. Traverse the list of dictionary keys until the percentage is greater than or equal to the random float from step 01. 
    03. Select the corresponding value to the key from step 02.
"""

import random

jobs = {}
file = open("occupations.csv").read().strip()
listOfJobs = file.split("\n")
counter = 0.0

for job in listOfJobs:
    t = job.split(",")
    counter = round(counter + float(t[-1]), 1)  # Rollover percentage
    
    # In case there is s "," in the occupation name
    jobstr = ""
    for x in range(0, len(t) - 1):
        jobstr = jobstr + t[x]
    
    jobs[counter] = jobstr

def trial():
    rando = (random.randint(1, 998) / 10.0) 
    for x in list(jobs.keys()):
        if x >= rando:
            chosen = jobs[x]
            break
    
    # Line for  Testing
    jobTest[chosen] = jobTest[chosen] + 1


## Testing Stuff
jobTest = {}
numOfTests = 1000000

for jobName in jobs.values():
    jobTest[jobName] = 0

for test in range(numOfTests):
    trial()

for k in list(jobTest.keys()):
    jobTest[k] = round(float(jobTest[k]) * 100 / numOfTests, 1)

print(jobTest)  

## End of Testing