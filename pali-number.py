import math

class Solution:
  def reverse(self, x: int) -> int:
    res = 0
    
    
    while (x > 0):
      # print('f=', factor)
      r = x % 10
      x = math.floor(x / 10)
      
      res = (res * 10) + r
      
    if ((res < -2147483648) or (res > 2147483647)):
      return 0
    else:
      return res
  
  
  def isPalindrome(self, x: int) -> bool: 
    # p = x;
    if ((x < -2147483648) or (x > 2147483647)):
      return 0

    if (x < 0):  
      return False
    
    pp = self.reverse(x)
    
    return x == pp
  
  
s = Solution()

print('121 palin? ', s.isPalindrome(121))
print('-121 palin? ', s.isPalindrome(-121))
print('10 palin? ', s.isPalindrome(10))
print('1 palin? ', s.isPalindrome(1))
    
    
    