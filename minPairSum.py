class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = []
        for i in range(len(nums)):
             answer.append(nums[i] + nums[len(nums)-1-i])
        return max(answer)
