class Solution:
  def twoSum(self, nums: [int], target: int) -> [int]:
    print(nums)
    
    for i in range(len(nums)):
      
      for j in range(len(nums[i + 1:])):
        print('[i] = {0} [j] = {1}'.format(nums[i], nums[j]))
        # if ((nums[i] + n) == target):
           
      
      # if (target - n):
        
    # return [1]
  
sol = Solution()
sol.twoSum([1,2], 2)