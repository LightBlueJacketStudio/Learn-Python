
# Solution
"""
Solution
def searchRange(nums: List[int], target: int) -> List[int]:
        
    def search(x):
        lo, hi = 0, len(nums)           
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid+1
            else:
                hi = mid                    
        return lo
    
    lo = search(target)
    hi = search(target+1)-1
    
    if lo <= hi:
        return [lo, hi]
            
    return [-1, -1]
    # edge cases / impossible cases
    # normal cases


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(searchRange(nums, target))

"""

from typing import *
from collections import *


# i see O(log n) requirement: heap or binary search
# --> binary search is a good approach
# implement the binary search such that it returns the first occurance 
# of the given number

def searchRange(nums: List[int], target: int) -> List[int]:
    #null
    if not nums: return [-1, -1]
    # one element
    if len(nums) == 1: return [0,0] if nums[0] == target else [-1, -1]


    # defines a binsearch that returns the index of the first occurance
    # of a certain number
    def binSearch(target: int) -> int :
        # we assumes the array is sorted
        # define high and low for the bounds
        hi = len(nums) #used the variable of parent function
        # noticed that we didn't restrict the hi to be within the array
        # range, this is because if the target is larger than every elements
        # we would want to return the index where the target should be, which 
        # is the first element out of bound

        lo = 0
        # we don't need to protect lo and hi to be in bound,
        # because we are never using them as index to access the array
        pivot = 0

        #search loop
        # binary search must shrink the interval every iteration
        # because we are looking for lower bound, we must make sure
        # the pivot doesn't stuck and not progressing
        
        while hi > lo: # while we still have a range to find
            # select a pivot index
            pivot =  lo + (hi - lo) // 2 # use integer devision here
            if nums[pivot] < target: 
            # if the value at pivot is smaller than target
            # we push the lo to pivot + 1
                lo = pivot + 1 
            else: # the pivot value is greater than or equal to the target
                # we drop the hi to pivot, pivot might be an answer 
                hi = pivot
        # at this point the hi <= lo, meaning we have squeezed to the last possible range
        return lo # always return the lower bound
    
    first = binSearch(target)
    last = binSearch(target + 1) - 1
    # the trick here is to use the fact that binsearch always give the lowest index
    # if we search for target +1, then whatever the index -1 will be the last occurance 
    # of the target (assume it's in the array at least once, we need to check value later)

    return [first, last] if first < len(nums) and nums[first] == target else [-1, -1]
     # if we get a nums[lo] != target, that means the value is not found


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    
    nums = [5,7,7,8,8,10]
    target = 6

    nums = []
    target = 0

    nums = [1]
    target = 1

    nums = [2,2]
    target = 2
    print(searchRange(nums, target))

