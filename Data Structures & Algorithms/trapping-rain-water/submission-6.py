class Solution:
    def trap(self, height: List[int]) -> int:
#at each index find the maximums on both lefts and rights,
#take the minis of them and substract height[i]
        water = 0 
        l, r = 0, len(height)-1 
        max_L, max_R = 0, 0

        while l<=r:
            max_L = max(height[l], max_L)
            max_R = max(height[r], max_R)
            res = min(max_L, max_R)-min(height[l], height[r])
            if res>0:
                water += res 
            if height[l]<=height[r]:
                l +=1 
            else:
                r -=1 
        return water
            