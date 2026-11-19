class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map1 = {}

        for i in range(len(names)):
            map1[i] =[heights[i], names[i]]

        res = sorted(map1.values(),reverse=True) 
        ans = []
        for person in res:
            ans.append(person[1])
        return ans

        