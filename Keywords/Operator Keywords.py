""" 
--------and, or, not, in, is-----------
and Keyword  return 'True' if both the operands are 'True'
or Keyword return 'True' if at least one operand is 'True'
not keyword returns 'True' if the expression is 'True', and vice versa.
"""

a = True
b = False

print(a and b)
print(a or b)

print(not a)
print(not b)



"""
in keyword (membership operator)
Check if a value exists in a sequence (like a list, tuple, or string). 
It returns True if value is found.
"""

# example 1
print(3 in [1,2,3])

# example 2
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")