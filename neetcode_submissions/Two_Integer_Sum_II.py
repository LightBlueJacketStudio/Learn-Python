from typing import *
from collections import *
"""
Given an array of integers numbers 
that is sorted in non-decreasing order. -> from small to large

Return the indices (1-indexed) of two numbers, 
[index1, index2], such that they add up to a 
given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, 
therefore you may not use the same element twice.

There will always be exactly one valid solution
Your solution must use O(1) additional space.
"""
# general idea
# solution must use o(1) space
# sorted , means bi-search could be used
# 1-index might be a hint

# use binary search for each element?
# two pointers from the middle, since the array is sorted
# we add the two elements together, if it's bigger -> move the left (total gets smaller)
# if it's smaller -> move the right (the total gets bigger)

## update, the pointers should start from both ends and not middle
# since the pair might be on either halfs, the starting from middle won't
# work in this case

# algorithm ?
# two pointers
# early return is possible since only one pair exists

# Your solution must use O(1) additional space
# time complexity
# since we only go through the list at most one time O(N)
# where the middle two elements are a pair
# by starting from both ends, we can only increase by moving the left pointer up 
# and can only increase by moving the right pointer down, so no pair is missed 

# space complexity
# restricted to O(1), not storing the list element indefinitely

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
                
        # edge cases / impossible cases
        if not numbers: return [] # if the input array is None

        # normal cases
        length = len(numbers) # used to determine the starting index for pointers
        pointerL = 0 # first element
        pointerR = length - 1 # last element

    #    pointerL = length // 2 # use integer division for index
    #    pointerR = pointerL + 1 # start with the middle elements
        sum = -1 # variable for stroing the sum
        
        while pointerL < pointerR: # while no overlap
            sum = numbers[pointerR] + numbers[pointerL] # get the sum
            if sum == target: # found the pair
                return [pointerL+1, pointerR+1] # return the list in the correct order
            elif sum < target: # means we need to increase the total
                # move the left pointer 
                pointerL += 1
            else: # means sum > target, we need to decrease the total
                # move the right pointer
                pointerR -= 1

        return [] # no pair is found, not possible in this problem

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    numbers = [1,2,3,4]
    target = 3
    numbers=[2,3,4]
    target=6
    print(sol.twoSum(numbers, target))
    

