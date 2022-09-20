def string_times(str, n):
  return str * n

##

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[0:3] * n

##

def string_bits(str):
  index = 0
  result = ""
  for e in str:
    if index % 2 == 0:
      result = result + e
    index = index + 1
  return result

##

def string_splosion(str):
  result = ""
  for x in range(0, len(str) + 1):
    result = result + str[0:x]
  return result

##

def last2(str):
  counter = 0
  last = str[-2:len(str)]
  for x in range (0,len(str)-2):
    if str[x:x+2] == last:
      counter = counter + 1
  return counter

##

def array_count9(nums):
  counter = 0
  for e in nums:
    if e == 9:
      counter = counter + 1
  return counter

##

def array_front9(nums):
  if len(nums) < 4:
    for e in nums:
      if e == 9:
        return True
  else:
    for x in range(0,4):
       if nums[x] == 9:
         return True
  return False

##

def array123(nums):
  for x in range (0, len(nums)-2):
    if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3:
      return True
  return False

##

def string_match(a, b):
  if (len(a) < len(b)):
    shortest = a
    longest = b
  else:
    shortest = b
    longest = a
  
  counter = 0
  for x in range (0, len(shortest) - 1):
    if shortest[x] == longest[x] and shortest[x+1] == longest[x+1]:
      counter = counter + 1
  
  return counter
  
##
