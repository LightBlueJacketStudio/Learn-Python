from typing import *
from collections import *

# general idea

# since we can assume only one pair exist, we can return as soon as we found a pair

# algorithm ?
# use a dict to store the residual, and run through the list to see if any number is 
# found in the dict
# the residual is the key and the value is the index of the element that 
# needs the residual
# when returning, we retrive the value of that specific key, and combine with the 
# key of the current element as the final output

# time complexity
# O(N), we only go through the list at most once

# space complexity
# O(N), in case of the first and the last elements are the pair

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # edge cases / impossible cases
        # either input is None, return empty list
        if not nums: return []  # target could be 0
        dict = {} # empty dictionary for storing pairs
        # residual = 0 # variable to store the conter part of a number
        # normal cases
        for index, num in enumerate(nums):
            if num in dict: # means we found a pair
                index1 = dict.get(num) # retrive the index
                return [index1, index] # we can use index1 at front directly
                # since the smaller index is always in the dict first
            else:
                dict[target - num ] = index # store the current index as the value
                # under the key of the residual


        return [] # if no pair is found, not possible in the problem tho

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    nums = [3,4,5,6]
    target = 7
    nums = [4,5,6]
    target = 10
    nums = [5,5]
    target = 10
    nums=[0,4,3,0]
    target=0
    print(sol.twoSum(nums, target))
    

