class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l1=list(nums)
        for a in nums:
            l1.append(a)
        return l1