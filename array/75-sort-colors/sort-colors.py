class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     Bucket Sort    
    #     count0 = 0
    #     count1 = 0
    #     count2 = 0

    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             count0+=1
    #         elif nums[i] == 2:
    #             count2+=1
    #         else:
    #             count1+=1

    #     for i in range(len(nums)):
    #         if (i < count0 and i >=0):
    #             nums[i] = 0
    #         elif i >= count0 and (i <= count0 + count1 - 1):
    #             nums[i] = 1
    #         else:
    #             nums[i] = 2

    #         # 0 - 0, count0-1
    #         # 1 - count0, count0 + count1 - 1
    #         # 2 - count0 + count1, count0 + count1 + count2 - 1

    

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0

        l = 0
        r = len(nums)-1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while(i <= r):
            if nums[i] == 0:
                swap(l, i)
                l+=1
            elif nums[i] == 2:
                swap(i, r)
                r-=1
                i-=1
            i+=1
        

        