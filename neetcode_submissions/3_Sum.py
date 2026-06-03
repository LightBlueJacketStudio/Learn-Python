from typing import *
from collections import *

""" Problem:
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order.
"""
# general idea
# problem asked to return the value, not the index 
# => we can sort the array first
# sum should be 0, meaning we need to have 
# at least one negative and at least one positive, 
# unless it's all 0

# divide and conquer?
# lock in one element, and see if we can find a pair that
# adds up to the negative counter part, or 0 if it's 0


# algorithm ?
# for every element, we use two pointers to find if any two elements
# add up to the negative counter part, or 0 if the element == 0

# time complexity
# O(N^2)

# space complexity
# O(1) we only stores the triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # edge cases / impossible cases
        if not nums or len(nums) < 3 : return [] 
        # if the input is None or has less than 3 elements

        # normal cases
        nums.sort() # sort the array first, so we can use two pointers
        result = []

        pointerL = 0
        pointerR = 0
        residual = 0 # the target for the two pointers
        sum = 0 # store the temporary sum of the two element

        for index, num in enumerate(nums):
            residual = -1 * num # also covers the case of 0
            pointerL = 0 # start with the first element
            pointerR = len(nums) - 1 # last element

            while pointerL < index and index < pointerR:
                sum = nums[pointerL] + nums[pointerR]
                if sum == residual: # found a pair
                    if [nums[pointerL], num, nums[pointerR]] not in result:
                        result.append([nums[pointerL], num, nums[pointerR]])
                    pointerL += 1
                    pointerR -= 1 # remember to move the pointers 
                    # when a solution is found
                elif sum < residual: # means we need to increase
                    # move left
                    pointerL += 1
                    # if the right is already at it's limit (>= index) 
                    # then while loop would break
                else: # means sum > residual, need decrease
                    # we need to move the right
                    pointerR -= 1


        return result if result else [] 
        # return result or [] if no pair is found

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    nums = [-1,0,1,2,-1,-4]
    nums = [0,1,1]
    nums = [0,0,0]
    nums=[0,0,0,0]
    print(sol.threeSum(nums))