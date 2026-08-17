from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        final = []
        for i in range(len(strs)):
            d["".join(sorted(strs[i]))].append(strs[i])
        for sort in d:
            final.append(d[sort])
        return final
            
            



        