"""
JFCCC: Fang Chen, Jeff Chen
Soft Dev, pd 2

DISCO:
Access dict items w/ dictName[key] or dictName.get(key())
random.randint(a,b) is inclusive of a and b
random.randrange(start, stop, step) will never >= stop regardless of how large step is
random.randrange(stop) gives a random int from [0, stop) 
QCC:
Why does...

    from random import seed
    from random import randint
    for _ in range(2):
        print(randint(0, 2))

... only print 2 [newline] 0?

Why is random.randint(a,b) inclusive of a and b when the convention is that it should be exclusive to b?

OPS Summary:
1. Dictionary krewes with elements period:[list of devos]
2. Pick a random period and select the corresponding list from krewes
3. Pick a random devo from said list

"""
import random

# krewes0 = {2:["Jeff", "Fang"], 7:["7Devo1", "7Devo2"], 8:["8Devo1", "8Devo2"]}
# print((krewes[2])[random.randint(0,1)])

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }
period = [2, 7, 8]
krewe = krewes[period[random.randint(0,2)]] 
# print(krewe[random.randint(0,len(krewe)-1)])


# print(random.randrange(10))

print(random.randrange(1, 10, 3))




