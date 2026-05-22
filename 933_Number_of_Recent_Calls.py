"""
class RecentCounter:

    def __init__(self):
        self.times = deque()

    def ping(self, t: int) -> int:
        self.times.append(t)
        while self.times and self.times[0] < t - 3000:
            self.times.popleft()
        return len(self.times)

solution
"""
from typing import *
from collections import *

# general idea

# use deque as the container, because once the old request
# is passed, they can be safely removed

# algorithm ?

# time complexity
# O(n - valid request)

# space complexity




class RecentCounter:

    def __init__(self):
        self.counter = deque() # use deque as counter

    def ping(self, t: int) -> int:
        # edge cases / impossible cases
        # normal cases
        self.counter.append(t) # add the new request

        while self.counter and self.counter[0] < t-3000:
            self.counter.popleft()
        
        return len(self.counter)


        pass

if __name__ == "__main__":
    print()

