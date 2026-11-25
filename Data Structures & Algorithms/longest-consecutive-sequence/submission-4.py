class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       n_set=set(nums)
       max_l,l=0,0
       for i in n_set:
        if i-1 not in n_set:
            start=i
            l=1
            while start+1 in n_set:
                l+=1
                start+=1
            max_l=max(max_l,l)
       return max_l if max_l else 0




          