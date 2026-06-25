class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}
#this is using hashmap. the simplest one, 
#problem asks you for using FLoyd's algo. thats the only catch
        for i in range(len(nums)):
            if nums[i] in hm:
                return nums[i]
            else:
                hm[nums[i]] = i 