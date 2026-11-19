class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {} 
        map[5], map[10], map[20] = 0, 0, 0
        for i in range(len(bills)):
            map[bills[i]] = map.get(bills[i], 0)+1 
            
            if bills[i] == 10:
                if map[5]:
                    map[5] -= 1
                else: 
                    return False 
            if bills[i] == 20:
                if map[5] and map[10]:
                    map[5] -= 1
                    map[10] -= 1 
                elif map[5] >= 3:
                    map[5] -= 3 
                else: 
                    return False 
        return True
                