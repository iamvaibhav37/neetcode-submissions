class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0 
        for ops in logs:
            if ops == "../":
                count = max(0, count-1)
            elif ops == "./":
                count = count 
            else:
                count += 1 
        return count
