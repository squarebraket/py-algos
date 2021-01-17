class Solution:
    def romanToInt(self, s: str) -> int:
      # Symbol       Value
      # I             1
      # V             5
      # X             10
      # L             50
      # C             100
      # D             500
      # M             1000
      
      romans = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
      exc = ['V', 'X', 'L', 'C', 'D', 'M']
      subtractors = { 'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M'] }
      total = 0
      prevRn = ''
      
      for rn in s:
        curVal = romans[rn]
        
        if (rn in exc):
          if ((prevRn in subtractors)):
            affected = subtractors[prevRn]
            if (rn in affected):
              prevVal = romans[prevRn]
              total -= prevVal
              total += (curVal- prevVal)
              continue; 
              
        total += curVal
          
        prevRn = rn
        
      return total
      
s = Solution()

print('int=', s.romanToInt('I'))
print('int=', s.romanToInt('II'))
print('int=', s.romanToInt('III'))
print('int=', s.romanToInt('IV'))
print('int=', s.romanToInt('IX'))
print('int=', s.romanToInt('LVIII'))
print('MCMXCIV=', s.romanToInt('MCMXCIV'))
print('DCXXI=', s.romanToInt('DCXXI'))
