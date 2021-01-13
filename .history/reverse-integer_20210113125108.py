import math

class Solution:
  def reverse(self, x: int) -> int:
    result = []
    res = 0
    
    if ((x < -2147483648) or (x > 2147483647)):
      return 0
    
    sign = 1
    if (x < 0):
      sign = -1
      x *= -1
      
    while (x > 0):
      # print('f=', factor)
      r = x % 10
      x = math.floor(x / 10)
      
      res = (res * 10) + r
      
    res *= sign
    
    if ((res < -2147483648) or (res > 2147483647)):
      return 0
    else:
      return res
  
  
  

s = Solution();
print('solution =', s.reverse(21))
print('solution =', s.reverse(11))
print('solution =', s.reverse(1))
print('solution =', s.reverse(100))
print('solution =', s.reverse(-21))
print('solution =', s.reverse(123))