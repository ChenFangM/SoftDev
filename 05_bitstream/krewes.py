"""
RANDO: Fang Chen, Julia Lee
Soft Dev, pd 2
K05 -- Krewes
2022-09-28
time spent: (classtime) 1.5 hrs

DISCO: 
    open(fileName.txt) does not return a String.
    You can get the text of the file in String format by calling (open(fileName.txt)).read()
    Str.split("<splitter>") splits a string and returns a list of substrings, not including the splitters
QCC:
    Is there an easy way to split with multiple "<splitters>"?
    What is the error:
        Need type annotation for "krewes"?
OPS Summary:
    1. Open krewes.txt and read it (convert to a str) (Utilize Str.strip() to remove newline)
    2. Split the string by "@@@", returning a list of "pd$$$devo$$$ducky"
    3. Run a for loop traversing the list, and splitting each string by "$$$" so that you get a new list with pd in index 0, devo in index 1, ducky in index 2
    4. Append the sublist with just devo and ducky onto the krewes dictionary with the key of pd.
"""
import random

krewes = {}

file = open("krewes.txt")
txt = file.read().strip()
splitCorr = txt.split("@@@")

for x in splitCorr:
    t = x.split("$$$")     # t = [pd, name, ducky]
    if int(t[0]) not in list(krewes.keys()):
        krewes[int(t[0])] = [t[1:]]
    else:
        krewes[int(t[0])].append(t[1:])
    

period = random.choice(list(krewes.keys()))
krewe = random.choice(krewes[period])
print(f"Pd {period} : {krewe}") 
print(f"krewes: {krewes}")