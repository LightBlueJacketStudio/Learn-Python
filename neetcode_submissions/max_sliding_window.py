from typing import *
from collections import *

""" Problem:
You are given an array of integers nums and an integer k.
There is a sliding window of size k that 
starts at the left edge of the array. 
The window slides one position to the right 
until it reaches the right edge of the array.

Return a list that contains the maximum element 
in the window at each step.
"""

# general idea
# determine the max of the first window once
# then each time we move the window, 
# we drop the left most and compare the new element with
# the max we already had 

# in case of teh left most element is always the max we 
# would be calculating the max over and over again :(

# algorithm ?
# use dequeue to have a sorted queue
# keep the front as the maximum of the current window
# discard every element from the right hand side 
# that is smaller than the new element
# so that we are sure every element added is smaller than
# all the elements in front of it

# we also constantly check if the current max is still within 
# range by checking the index (which is what we store)
# once we grew the window, we pop the first element as our max
# for every new element


# time complexity
# we only go through the list once -> O(N)

# space complexity
# we store maximum of K elements, where K is the window size
# O(K)
# worst case: the list is sorted in desc order

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # edge cases / impossible cases
        if not nums or not k: return []
        # if the number list is empty or k is 0

        # normal cases
        buffer = deque() # initialze our buffer for storing the max
        result = []

        for index, num in enumerate(nums):
            # check index of max
            if buffer and buffer[0][0] < index - k + 1: 
            # means the max is out of window
                buffer.popleft() # drop the max, second max got up
            
            # drop anything that is less than the current element
            while buffer and nums[buffer[-1][0]] < num:
                buffer.pop()
            
            # insert the current element
            buffer.append((index, num)) # we store the index, not the value

            # check if the window is big enough to generate result
            if index >= k-1:
                result.append(nums[buffer[0][0]])
            

        return result

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    nums = [1,2,1,0,4,2,6]
    k = 3
    print(sol.maxSlidingWindow(nums, k))