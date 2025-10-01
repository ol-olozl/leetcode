class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums)-1
            target = 0 - nums[i]

                
            while left < right:

                s = nums[left] + nums[right]
                if s == target:
                    ret.append([nums[i], nums[left], nums[right]])

                    val_l = nums[left]
                    val_r = nums[right]
                    while left<right and nums[left] == val_l:
                        left += 1
                    while left<right and nums[right] == val_r:
                        right -= 1
                elif s < target:
                    left += 1
                elif s > target:
                    right -= 1

        return ret
