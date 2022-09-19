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
