class Solution:

    def encode(self, strs: List[str]) -> str:
        for a in range(len(strs)):
            wrd="*7agdga^7"+strs[a]+'^7xd'
            strs[a]=wrd
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        ls=[]
        strs=s.split('^7')[1::2]
        return strs 
