class Solution:
  def reverse(self, x: int) -> int:
    result = []
    
    if ((x > 2147483647) or (x < -2147483648)):
      return 0
    
    factor = 0
    while (x > 0):
      r = x % 10
      x = x - (x % 10)
      
      
    return 1
  
  
  

s = Solution();
print('solution =', s.reverse(2147483648))
print('solution =', s.reverse(-2147483649))