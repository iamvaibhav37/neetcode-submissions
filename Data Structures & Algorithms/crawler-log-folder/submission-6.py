class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0 
        for ops in logs:
            if ops == "../":
                if count>0:
                    count -= 1
            elif ops == "./":
                continue
            else:
                count += 1 
        return count
