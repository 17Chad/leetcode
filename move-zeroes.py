'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution(object):
    def moveZeroes(nums):
        # No creating a new list, must do in place
        prev_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                hold = nums[prev_index]     # hold = 0 this will increment with us finding 0's
                
                nums[prev_index] = nums[i]  # index 0 and 1 are now "1, 1"
                nums[i] = hold              # index 0 and 1 are not "1, 0"
                prev_index += 1 
        return nums

if __name__ == "__main__":
    solution = Solution
    nums = [0,1,0,3,12]

    print(solution.moveZeroes(nums))