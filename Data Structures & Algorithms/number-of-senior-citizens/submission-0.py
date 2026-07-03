class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passan in details:
            num = 0
            for j in range(11,13):
                
                num = num * 10 + int(passan[j])
            if num > 60:
                count += 1
        return count

