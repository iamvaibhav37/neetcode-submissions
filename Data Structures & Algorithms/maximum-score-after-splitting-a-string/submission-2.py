class Solution:
    def maxScore(self, s: str) -> int:
        count1, count2, count  = 0, 0, 0
        total = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:len(s)]

            count1 = left.count("0")
            count2 = right.count("1")
            total = max(total, count1+count2)
        #     for _ in range(len(left)):
        #         if left[_] == "0":
        #             count1 += 1 
        #     for _ in range(len(right)):
        #         if right[_] == "1":
        #             count2 += 1 
        #     sum1 = count1 + count2 
        #     count = max(sum1, count)
        return total
            