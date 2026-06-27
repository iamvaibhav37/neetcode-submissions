class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()

        l, r = 0, len(arr)-1
        
        if (len(arr)%2) == 0:
            mid1 = (l + r)//2
            mid2 = mid1 + 1
            return (arr[mid1] + arr[mid2])/2
        else:
            return arr[(l+r)//2]


        