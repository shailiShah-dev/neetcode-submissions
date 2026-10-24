class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1=sorted(s)
        ls2=sorted(t)
        if len(ls1)==len(ls2) and ls1==ls2:
            return True
        return False

