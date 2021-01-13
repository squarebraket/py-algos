import math


def merge(left, right):
  temp = []
  
  while (len(left) > 0 and len(right) > 0):
    if (left[0] < right[0]):
      temp.append(left.pop(0))
    else:
      temp.append(right.pop(0))
      
  return temp + left + right

def sortMerge(arr):
  
  if (len(arr) < 2):
    return arr
  
  middle = maht.floor(len(arr) / 2)
  left = arr[0: middle]
  right = arr[middle:]
  
  return merge(mergeSort(left), mergeSort(right))

class Solution:
  def sort(nums):
    
    
    
  def twoSum(self, nums: [int], target: int) -> [int]:
    result = []
    print(nums)
    
    for i in range(len(nums)):
      j = i + 1
      
      while j < len(nums):
        print('[i] = {0} [j] = {1} j = {2}'.format(nums[i], nums[j], j))
        if ((nums[i] + nums[j]) == target):
          result.append(i)
          result.append(j)
        
        j = j + 1
          
      
      # if (target - n):
        
    print('r = {0}'.format(result))
    return [1]
  
sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)