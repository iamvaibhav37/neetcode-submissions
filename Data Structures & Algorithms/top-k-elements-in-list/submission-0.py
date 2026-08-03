class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Step 2: Bucket sort (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in freq:
            count = freq[num]
            buckets[count].append(num)
        
        # Step 3: Traverse from high freq → low freq
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res