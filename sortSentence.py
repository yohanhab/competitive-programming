class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = s.split()
        list2 = []
        list3 = []

        answer = ''

        for i in range(len(list1)):
            list2.append(0)
        
        for i in list1:
            num = int(i[len(i) -1])
            list2[num-1] = i

        for i in list2:
            i = i[:-1]
            list3.append(i)
            
        answer = " ".join(list3)
        return answer
