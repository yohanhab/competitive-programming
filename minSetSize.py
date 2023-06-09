class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        answer = 0
        value = Counter(arr)
        listt = list(value.values())
        listt.sort(reverse=True)
        length = len(arr)
        final = len(arr) //2
        for x in listt:
            if length > final:
                length -=x
                answer +=1
            else:
                break
        return answer
