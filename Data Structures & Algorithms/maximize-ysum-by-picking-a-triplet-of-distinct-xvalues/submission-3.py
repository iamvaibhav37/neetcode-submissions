class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        hm = {}

        for i in range(len(x)):
            if x[i] not in hm:
                hm[x[i]] = y[i]
            
            hm[x[i]] = max(hm[x[i]], y[i]) #maps the current value at x[i] to the gratest y[i] comapring its value with already stored value

        values = list(hm.values())
        values.sort()
        if len(values)<3:
            return -1
        else:
            return sum(values[-3:])  #that [-3:]tells to give last 3 elements. 