"""
RANDO: Fang Chen, Julia Lee
Soft Dev, pd 2
K06 - Divine your Destiny!
2022-10-03
time spent:

DISCO:

QCC:

HOW THIS SCRIPT WORKS:


Total,99.8
"""

jobs = {}
file = open("occupations.csv").read().strip()
listOfJobs = file.split("\n")
counter = 0.0

for job in listOfJobs:
    t = job.split(",")
    counter = round(counter + float(t[-1]))  # Rollover percentage
    
    # In case there is s "," in the occupation name
    jobstr = ""
    for x in range(0, len(t) - 1):
        jobstr = jobstr + t[x]
    
    jobs[counter] = jobstr
    
print(jobs)