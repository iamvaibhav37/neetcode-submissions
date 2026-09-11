class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] 

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]: 
                    a = nums2[j]
                    for j in range(j, len(nums2)):
                        if nums2[j] > a:
                            res.append(nums2[j])
                            break
                    else:
                        res.append(-1)
        return res