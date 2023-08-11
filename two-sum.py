'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

# Testcase
nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {} # initiaize, store number and its index
        for i, num in enumerate(nums):
            complement = target - num # target we want to find: 9 - 2 = 7

            if complement in num_map: 
                return [num_map[complement], i] # Return indicides of the two numbers
            num_map[num] = i  # num_map[2] = 0
        return []
# This solution runs in O(n) time, where n is the number of elements in nums, because we traverse the list once and dictionary operations (insertions and lookups) are generally O(1).
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums, target))

