class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []   #monotonic stack. 
        greater = {} 

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num
            
            stack.append(num)
        
        for num in stack:
            greater[num] = -1 
        
        return [greater[num] for num in nums1]
            
            