import math


class Solution:
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
    

    def twoSum(self, numsUn: List[int], target: int) -> List[int]:
        nums = self.mergeSort(numsUn)
        result = []
        prevDiff = {}

        # print('nums = {0}'.format(nums))

        for i in range(len(nums)):

          diff = target - nums[i]
          # print('diff = ', diff)

          if (nums[i] in prevDiff):
            result.append(i)
            result.append(prevDiff.get(nums[i]))
          else:
            prevDiff[diff] = i

        # print('r = {0}'.format(result))
        # print('prevDiff = {0}'.format(prevDiff))
        return result
        
  
sol = Solution()
sol.twoSum([3, 2, 4], 6)