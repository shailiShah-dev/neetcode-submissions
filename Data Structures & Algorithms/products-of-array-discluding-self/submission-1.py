class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero_counter=0
        l=len(nums)
        ls=[0]*l
        for a in nums:
            if a==0:
                zero_counter+=1
            else:    
                prod*=a
        if zero_counter>1:
            return ls
        elif zero_counter==1:
            ls[nums.index(0)]=prod
            return ls
        else:
            for a in range(l):
                ls[a]=prod//nums[a]
        return ls



        