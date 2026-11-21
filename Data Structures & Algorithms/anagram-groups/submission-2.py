class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in rec:
                rec[key]=[]
            rec[key].append(i)
        return list(rec.values())