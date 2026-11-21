class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec={}
        for i in strs:
            my_arr=[0]*26
            for a in i:
                my_arr[ord(a.lower())-97]+=1
            key=tuple(my_arr)
            if key not in rec:
                rec[key]=[i]
            else:
                rec[key].append(i)
        return list(rec.values())