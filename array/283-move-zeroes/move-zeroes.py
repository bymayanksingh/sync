class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        f = 0
        for i in range(n):
            if nums[i] != 0:
                nums[f] = nums[i]
                f = f + 1
        
        for i in range(f, n):
            nums[i] = 0

        return nums