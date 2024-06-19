class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            hash[nums[i]] = i
        return False

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False