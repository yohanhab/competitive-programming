class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
      if len(changed)==0 or len(changed)%2!=0 :
        return [] 
      
      res=[]
      counts=collections.Counter(changed)

      
      if counts.get(0):
        if counts[0]%2==0:
          res.extend([0]*(int(counts[0]/2)))
          counts[0]=0
        else:
              return []
      
      
      
      for x in sorted(counts): 
        if counts[x]>0:
          if x/2 in counts and counts[x/2]>0: 
            minLen=min(counts[x],counts[x/2])
            res.extend([int(x/2)]*minLen)
            counts[x]-=minLen
            counts[x/2]-=minLen
          elif x*2 in counts and counts[x*2]>0:
            minLen=min(counts[x],counts[x*2])
            res.extend([x]*minLen)
            counts[x]-=minLen
            counts[x*2]-=minLen
          else:
            return []
      
      if sum(counts.values())==0:
            return res
      else:
            return []
