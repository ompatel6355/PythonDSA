class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+ nums[j]+ nums[k] == 0:
                        ans.append(nums[i], nums[j], nums[k])

s = Solution()
nums = [-1,0,1,2,-1,-4]
s.threeSum(nums)
