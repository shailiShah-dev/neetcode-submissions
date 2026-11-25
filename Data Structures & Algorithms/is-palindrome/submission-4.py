class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<=j:
            if not s[i].isalpha() and not s[i].isdigit():
                i+=1
            elif not s[j].isalpha() and not s[j].isdigit():
                j-=1
            else:
                if s[i].isdigit() and s[j].isdigit() and s[i]==s[j]:
                    i+=1
                    j-=1
                elif s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True
