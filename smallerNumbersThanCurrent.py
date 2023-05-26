class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        assert 2 <= len(nums) <= 500
        answer = [0*i for i in range(len(nums))]
        noRepetition = dict()
        for i in range(len(nums) -1, 0, -1):
            assert 0 <= sort[i] <= 100
            if sort[i] > sort[i - 1] :
                noRepetition[sort[i]] = i
                
        noRepetition[sort[0]] = 0
        for i in range(len(nums)):
            answer[i] = noRepetition.get(nums[i])
        
        return answer
