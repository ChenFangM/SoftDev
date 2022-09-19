# Warmup 1

def sleep_in(weekday, vacation):
  return not weekday or vacation
  
##

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

##

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b

##

def diff21(n):
  if n > 21:
    return 2 * (abs(n - 21))
  else:
    return abs(n - 21)

##

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

##

def makes10(a, b):
  return a == 10 or b == 10 or a+b == 10

##

def near_hundred(n):
  return (n >= 90 and n <= 110) or ( n >= 190 and n <= 210)

##

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)
# Warmup

def sleep_in(weekday, vacation):
  return not weekday or vacation
  
##

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

##

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b

##

def diff21(n):
  if n > 21:
    return 2 * (abs(n - 21))
  else:
    return abs(n - 21)

##

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

##

def makes10(a, b):
  return a == 10 or b == 10 or a+b == 10

##

def near_hundred(n):
  return (n >= 90 and n <= 110) or ( n >= 190 and n <= 210)

##

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)

##
  
def not_string(str):
  if str[0:3] != "not":
    return "not " + str
  else:
    return str
  
##

def not_string(str):
  if str[0:3] != "not":
    return "not " + str
  else:
    return str
  
##

def front_back(str):
  if len(str) < 2:
    return str
  else: 
    return str[-1] + str[1:-1] + str[0]
  
##

def front3(str):
  if len(str) <= 3:
    return str * 3
  else:
    return str[0:3] * 3

##
  
def not_string(str):
  if str[0:3] != "not":
    return "not " + str
  else:
    return str
  
##

def not_string(str):
  if str[0:3] != "not":
    return "not " + str
  else:
    return str
  
##

def front_back(str):
  if len(str) < 2:
    return str
  else: 
    return str[-1] + str[1:-1] + str[0]
  
##

def front3(str):
  if len(str) <= 3:
    return str * 3
  else:
    return str[0:3] * 3
