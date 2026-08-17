class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = k
        dic = {}
        final = []
        for val in nums:
            dic[val] = dic.get(val, 0) + 1
        while counter != 0:
            most = 0
            mostk = 0
            for key in dic:
                if dic[key] > most:
                    most = dic[key]
                    mostK = key
            final.append(mostK)
            dic.pop(mostK, None)
            counter -= 1
        return final
                
                
            
                