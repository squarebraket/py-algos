import math

class Solution:
  def reverse(self, x: int) -> int:
    result = []
    res = 0
    
    if ((x > 2147483647) or (x < -2147483648)):
      return 0
    
    sign = 1
    factor = 1
    if (x < 0):
      sign = -1
      x *= -1
      
    while (x > 0):
      r = x % 10
      x = math.floor(x / 10)
      
      res = (res * factor) + r
      
      factor *= 10
      
    return res * sign
  
  
  

s = Solution();
print('solution =', s.reverse(21))
print('solution =', s.reverse(11))
print('solution =', s.reverse(1))
print('solution =', s.reverse(100))
print('solution =', s.reverse(-21))