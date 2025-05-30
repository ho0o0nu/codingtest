class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            answer = [0] * len(nums)
            for i in nums:
                if nums[i] == 0:
                    prod = 1
                    for num in nums:
                        if num == nums[i]:
                            continue
                        prod *= num
                    answer[i] = prod
        else:
            answer = []
            prod = 1
            for num in nums:
                prod *= num
            for num in nums:
                answer.append(prod // num)
        
        return answer