class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        ans = []

        for i, n in enumerate(nums):
            if target - n in hashmap:
                ans.append(i)
                ans.append(hashmap[target - n])
                return ans
            else:
                hashmap[n] = i
        
        return ans
