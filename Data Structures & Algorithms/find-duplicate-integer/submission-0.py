class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        res = dict()

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] +=1
                return num

        