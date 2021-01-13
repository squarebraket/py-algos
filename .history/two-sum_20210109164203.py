class Solution:
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
          
      
      # if (target - n):
        
    print('r = {0}'.format(result))
    return [1]
  
sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)