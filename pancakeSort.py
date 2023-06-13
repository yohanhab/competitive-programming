class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer =[]
        i =0
        j =0
        max= len(arr)

        temp =[]
        while(j < len(arr)-1):
           i=0
           while(i < len(arr)):
              if(arr[i] ==max):
                  answer.append(i+1)
                  answer.append(len(arr)-j)
                  max = max-1
                  temp = arr[0:i+1]
                  temp.reverse()
                  temp = temp + arr[i+1:len(arr)-j]
                  temp.reverse()
                  arr = temp +arr[len(arr)-j:]
                
                  j = j+1
                  break
              i = i+1
       
        return answer
