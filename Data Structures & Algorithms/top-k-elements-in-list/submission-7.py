class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for a in nums:
            if a not in freq:
                freq[a]=1
            else:
                freq[a]+=1
        return [a[0] for a in sorted(freq.items(),reverse=True,key=lambda x:x[1])][:k]
