class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            answer = [0] * len(nums)
            for i, v1 in enumerate(nums):
                if v1 == 0:
                    prod = 1
                    for j, v2 in enumerate(nums):
                        if i == j:
                            continue
                        prod *= v2
                    answer[i] = prod
        else:
            answer = []
            prod = 1
            for num in nums:
                prod *= num
            for num in nums:
                answer.append(prod // num)
        
        return answer