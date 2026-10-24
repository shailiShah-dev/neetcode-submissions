class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1=sorted(s)
        ls2=sorted(t)
        if ls1==ls2:
            return True
        return False

