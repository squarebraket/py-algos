import math

class Solution:
  def reverse(self, x: int) -> int:
    result = []
    res = 0
    
    if ((x > 2147483647) or (x < -2147483648)):
      return 0
    
    factor = 1
    while (x > 0):
      r = x % 10
      x = math.floor(x / 10)
      
      res = res + (factor * r)
      
      factor 
    return 1
  
  
  

s = Solution();
print('solution =', s.reverse(2147483648))
print('solution =', s.reverse(-2147483649))