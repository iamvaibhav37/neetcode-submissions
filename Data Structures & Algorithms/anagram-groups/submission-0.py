class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        std = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {}
        for i in range(26):
            mapping[std[i]] = i

        for word in strs:
            count = [0]*26

            for ch in word:
                index = mapping[ch]
                count[index] += 1
            
            key = tuple(count)

            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]

        return list(hash.values())



        
        

        

