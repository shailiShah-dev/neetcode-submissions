class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rec={}
        for a in nums:
            if a in rec:
                rec[a]+=1
            else:
                rec[a]=1
        lis=sorted(rec.items(),key=lambda x:(x[1],x[0]))[::-1]
        return [lis[a][0] for a in range(k)]