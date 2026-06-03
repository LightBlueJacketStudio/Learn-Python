from typing import *
from collections import *

""" Problem:
Given two integers a and b, 
return the sum of the two integers 
without using the + and - operators.
"""

# general idea
# cannot use + or -
# use len() then

# algorithm ?

# time complexity
# O(1) since we just call len()
# space complexity
# O(n) since we will address N elements

#Neet code solution:
# bitwise operator: Xor handle the adding (^)
# and handles the carry bit (&)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # naive solution
        # # edge cases / impossible cases
        # if not a and not b: return 0 # a and b are both 0

        # # normal cases
        # turn = 1 # used to mark if teh sign needs to change

        # if a < 0 and b < 0: 
        #     a *= -1
        #     b *= -1
        #     turn = -1

        # # pick the small number to loop
        # small = min(a,b)
        # big = max(a,b)

        # list1 = [0] * big or []
        # if small >= 0:
        #     for _ in range(small):
        #         list1.append([0])
        # if small < 0:
        #     for _ in range(-1 * small):
        #         if list1 and turn != -1: list1.pop() # if we still have elements
        #         else: 
        #             turn = -1 # indicate negative
        #             list1.append([0])
        # return len(list1) * turn        
        # ================ Bitwise Solution ==================
        mask = 0xFFFF # represents ~ 1000, precise to 12 bits
        and_result = 1
        xor_result = 0
        neg = True if abs(min(a,b)) > max(a,b)else False
        var1 = a
        var2 = b
        # while we still have carry bits
        while and_result:
            xor_result = (var1 ^ var2) & mask # this would discard anything beyond 12 bits
            and_result = ((var1 & var2) << 1) & mask
            var1 = xor_result
            var2 = and_result
        
        return var1 if not neg else ~(var1 ^ mask)

if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    a = 4
    b = 7
    a=-1
    b=1
    a=0
    b=17
    a=-2
    b=0
    a=-12
    b=-8
    a=1000
    b=1
    print(sol.getSum(a, b))