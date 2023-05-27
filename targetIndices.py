class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        sort = sorted(nums)

        for i in range(len(sort)):
            if sort[i] == target:
                answer.append(i)

        return answer
