class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclid = []
        answer = []
        for i in range(len(points)):
            sqr = ((points[i][0]) **2 + (points[i][1]) **2) **(1/2)
            euclid.append([sqr ,points[i]])
         
        euclid = sorted(euclid)

        for i in range(k):
              answer.append(euclid[i][1])

        return answer
