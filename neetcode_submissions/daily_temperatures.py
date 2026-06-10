from typing import *
from collections import *

""" Problem:
You are given an array of integers temperatures
where temperatures[i] represents the daily temperatures 
on the ith day.

Return an array result where result[i] is 
the number of days after the ith day before 
a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature 
will appear for the ith day, set result[i] to 0 instead.
"""

# general idea
# the problem arises when the temperature is constantly decreasing
# meaning each element are actively counting and updating
# this would get inefficient when the array got long enough

# using a stack can solve this problem:
# by pushing we mean pushing the index
# for each element we push it into the stack, once we encouter
# a temperature bigger than the first element, we keep popping
# and calculate the difference until we see an element that is
# bigger than current or the stack is empty

# algorithm ?
# stack

# time complexity
# O(N), for any arrays
# space complexity
# O(N), happens for decs sorted arrays
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # edge cases / impossible cases
        if not temperatures: return []
        
        # normal cases
        stack = [] # use a list as a stack
        result = [0] * len(temperatures) 
        # strictly 1 to 1 relationship, use 0 as deault value

        for index, temp in enumerate(temperatures): 
            # get both index and value
            # compare with last and push the index
            while stack and temperatures[stack[-1]] < temp:
                item = stack.pop()
                result[item] = index - item # calculate the difference
            stack.append(index) # new element is appended anyways

        return result


if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    temperatures = [30,38,30,36,35,40,28]
    # expected: [1,4,1,2,1,0,0]

    temperatures=[89,62,70,58,47,47,46,76,100,70]
    # expected: [8,1,5,4,3,2,1,1,0,0]

    print(sol.dailyTemperatures(temperatures))