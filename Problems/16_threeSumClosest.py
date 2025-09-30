class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2] 

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if abs(temp_sum-target) < abs(ret-target):
                    ret = temp_sum

                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left += 1
                elif temp_sum == target:
                    return temp_sum


        return ret
