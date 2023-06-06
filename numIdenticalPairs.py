class Solution:
    def repition(self,num,nums):
            indecis = []
            for indx,value in enumerate((nums)):
                if num == value:
                    indecis.append(indx)
            return len(indecis) -1

    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        temp = nums.copy()
        visited = []
        for x in range(len(nums)):
            rept = self.repition(nums[x], temp)
            if nums[x] not in visited:
                answer += (sum(range(rept +1)))
            visited.append(nums[x])
            temp.remove(nums[x])

        return answer
