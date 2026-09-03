class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp]) 


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res = ""
        #binary search
        l, r = 0, len(self.timeMap[key]) - 1
        while l <= r:
            m = (l + r) // 2


            if self.timeMap[key][m][1] <= timestamp:
                res = self.timeMap[key][m][0]
                l = m + 1
            elif self.timeMap[key][m][1] > timestamp:
                r = m - 1
        return res
            
        

        
