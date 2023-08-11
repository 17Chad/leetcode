'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # solution will iterate until the array of strings is reversed
        # ["h","e","l","l","o"]
        # ["o","e","l","l","h"]
           #^              #^
        left_ptr = 0
        right_ptr = len(s) - 1 # because our index will start at 0 
        while left_ptr < right_ptr:
            hold = s[left_ptr]          # Holds the left pointer 
            
            s[left_ptr] = s[right_ptr]  # This is the swap
            s[right_ptr] = hold         # 

            left_ptr += 1   #moves right
            right_ptr -= 1  #moves left
        return s

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    solution = Solution()
    print(solution.reverseString(s))