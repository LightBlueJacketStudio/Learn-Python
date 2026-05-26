""" Solution
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        for diag in [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]:
            kk, dist = k, 0
            for ch in s:
                if ch in diag or kk:
                    dist += 1
                    kk -= ch not in diag
                else:
                    dist -= 1
                res = max(res, dist)
        return res

"""
# time complexity: O(n)
# space complexity: O(1)


# general idea
"""
longest man distance = furthest x + furthest y
changes allowed but limited: only change when necessary
the string is traversed in order: change can be greedy, no need to 
think about later effects

diagonal is the way to go

NW: change on S and E
NE: change on S and W

SW: change on N and E
SE: change on N and W

manhantan distance: maximum x + y
=> we use the majority of the diagnal from the string
to decide which way to go
=> since we probably want to optimize time complexity,
we search all four diagnal at once to avoid going through 
the string multiple times

by using diagnal, we allow 2 directions instead of just 1 like if we
used NESW as the goal
thus increase the length of guaranteed correct path
since the string is unchanged, and there's no rotation
the path that has the longest correct path from the start
would have the longest manhatan distance
"""

# algorithm ?
"""
use a  to hold each directions {(N,W), (N,E),...}
traverse through the list, if the direction is in the tuple we add 1
if not, we use one change, and add 1
if change is used up we just evaluate that to our manhantan distance
"""
# time complexity: O(n)
# space complexity: O(1)
# same for looping string 4 times or do 4 direction at once

from typing import *
from collections import *

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        # edge cases / impossible cases
        if not s: return 0 # if empty string is passed
        elif len(s) == 1: return 1 #if only one char then the distance is always 1


        # normal cases
        # first element: current distance
        # second element: remaining changes
        # third element: max distance
        tracker = [[0, k, 0] for _ in range(4)] # a list of 4 of [0,k]

        correct = [('N','W'), ('N','E'), ('S','W'), ('S','E')]
        for char in s:
            for index, diagnals in enumerate(correct):
                if char in diagnals: tracker[index][0] += 1
                elif tracker[index][1] > 0: 
                    tracker[index][0] += 1
                    tracker[index][1] -= 1
                else: 
                # meaning the char is not the direction we want
                # and we have no corrections left
                    tracker[index][0] -= 1
                
                #update max if needed
                if tracker[index][0] > tracker[index][2]:
                    tracker[index][2] = tracker[index][0]
                    
        return max(item[2] for item in tracker)  # use generator expression to feed Max  





if __name__ == "__main__":
    sol = Solution()
    
    # test cases
    s = "NWSE"
    k = 1
    # return 3

    s = "NSWWEW"
    k = 3
    # return 6

    print(sol.maxDistance(s,k))

