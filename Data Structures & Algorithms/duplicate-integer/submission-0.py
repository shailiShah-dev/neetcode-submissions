class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls=sorted(nums)
        for i in range(len(ls)-1):
            if ls[i]==ls[i+1]:
                return True
        return False