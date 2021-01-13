class Solution:
  def reverse(self, x: int) -> int:
    if (x > 2147483647 or x < -2147483648):
      return 0
    
    return 1
  
  
  

s = Solution();
print('solution =', s.reverse(1))