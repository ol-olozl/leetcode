class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in dct:
                return [dct[diff], idx]
            dct[val] = idx
