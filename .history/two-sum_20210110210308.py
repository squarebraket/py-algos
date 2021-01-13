import math


class Solution:
  
  def binarySearch(self, arr, target):
    startIndex = 0
    endIndex = len(arr) - 1
  
    while(startIndex <= endIndex):
      middleIndex = math.floor((startIndex + endIndex) / 2)
      
      if (target == arr[middleIndex]):
        return middleIndex
      
      if (target > arr[middleIndex]):
        startIndex = middleIndex + 1
        
      if (target < arr[middleIndex]):
        endIndex = middleIndex - 1
    
    return -1


  def merge(self, left, right):
    temp = []
    
    while (len(left) > 0 and len(right) > 0):
      if (left[0] < right[0]):
        temp.append(left.pop(0))
      else:
        temp.append(right.pop(0))
        
    return temp + left + right

  def mergeSort(self, arr):
    
    if (len(arr) < 2):
      return arr
    
    middle = math.floor(len(arr) / 2)
    left = arr[0: middle]
    right = arr[middle:]
    
    return self.merge(self.mergeSort(left), self.mergeSort(right))
    
  def twoSum(self, nums0: [int], target: int) -> [int]:
    nums = self.mergeSort(nums0)
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
  
  def twoSum2(self, nums0:[int], target: int) -> [int]:
    nums = self.mergeSort(nums0)
    result = []
    prevDiff = {}
    
    for i in range(len(nums)):
      
      diff = target - nums[i]
      
      if (diff in prevDiff):
        result.append(i)
        result.append(prevDiff.get(diff))
      else:
        prevDiff[diff] = i
    
    print('r = {0}'.format(result))
    print('prevDiff = {0}'.format(prevDiff))
    return result
  
sol = Solution()
sol.twoSum2([2, 15, 7, 11], 9)