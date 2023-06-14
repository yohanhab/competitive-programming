class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        value = list(num.values())
        value.sort(reverse=True)
        top = value[:k]
        answer = []
        for key in num.keys():
                if num[key] in top:
                    answer.append(key)
        return answer
