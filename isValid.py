class Solution:
    def isValid(self, s: str) -> bool:
        answer = []
        dict1 = {")":"(", "]":"[", "}":"{"}
        for ele in s:
            if ele in dict1:
                if answer and answer[-1] == dict1[ele]:
                    answer.pop()
                else:
                    return False
            else:
                answer.append(ele)
        if answer:
            return False
        return True
