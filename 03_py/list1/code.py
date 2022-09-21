##

def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

##

def same_first_last(nums):
  if len(nums) == 0:
    return False
  elif len(nums) < 2:
    return True
  return nums[0] == nums[-1]

##
