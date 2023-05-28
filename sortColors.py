class Solution:
    def sortColors(self, nums: List[int]) -> None:
        answer = sorted(nums)
        for i in range(len(answer)):
            if nums[i] != answer[i]:
                nums[i] = answer[i]
        
