from typing import *
from collections import *

""" Problem:
Given an integer array nums and an integer k, 
return the k most frequent elements within the array.

The test cases are generated such that the 
answer is always unique.

You may return the output in any order.
"""

# general idea
# use counter to count the freq -> build a dict
# use bucket sort, range of bucket would be K
# go through the dict to sort
# then stop at K elements from the tail

# algorithm ?
# use bucket sort to map frequencies

# time complexity
# counter -> O(N)
# bucket sort -> O(N) just mapping the frequency
# retrival -> O(N) just go through the bucket list
# O(N)
# space complexity
# O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # edge cases / impossible cases
        if (k < 0 
            or 
            not k or not nums): return [] 
        # k is 0, neg, or list is empty
        
        # normal cases
        count = Counter(nums) # create a counter object, where key = element, val = freq
        bucket = [[] for _ in range(len(nums) + 1)] 
        # list of list because some element might have the same freq
        # the range of bucket is N, in case of homogeneous list

        result = [] # for storing result to return

        # map the freq
        for number, value in count.items():
            bucket[value].append(number)

        # now we have the freq map
        for freq in range(len(bucket)-1, 0, -1): # from tha tail of the bucket
            result.extend(bucket[freq]) # extend: expand and add element one by one
            if len(result) >= k: break # break the loop once we hit the limit

        return result[:k]

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    nums = [1,2,2,3,3,3]
    k = 2
    nums = [7,7]
    k = 1
    print(sol.topKFrequent(nums, k))