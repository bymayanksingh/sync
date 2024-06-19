class Solution:
    # #brute
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         res.append(1)

    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if j != i:
    #                 res[i] = res[i] * nums[j]
    #     return res
        
    #with prefix and postfix array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        size = len(nums)
        result.append(p)

        for i in range(1, size):
            p = p*nums[i-1]
            result.append(p)
        p = 1

        for i in range(size - 1, -1, -1):
            result[i]*=p
            p*=nums[i]
        
        return result


        


