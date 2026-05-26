from typing import *
from collections import *

# allowed operation
# Fill either jug completely with water.
# Completely empty either jug.
# Pour water from one jug into another until 
# the receiving jug is full, 
# or the transferring jug is empty.

# target = the total amount of water both jugs combined after
# any operations
# return = is target possible to reach
def canMeasureWater(x: int, y: int, target: int) -> bool:

    capacity_A = x
    capacity_B = y
    total_capacity = capacity_A + capacity_B


    # edge cases / impossible cases
    # target is more than combined
    if target > total_capacity: 
        return False
    # target is one of the jug or conbined capacity
    elif target == capacity_A or target == capacity_B or target == total_capacity:
        return True

    # normal cases
    # so we are basically asking 
    # if -a * capacity_A + -b capacity_B + c * (x+y) = target
    # where -a * capacity_A + -b capacity_B <= c * (x+y)
    # # ^ well target is positive so we don't really need to check that 
    # [a,b,c] as [int, int, double] exists

    # we can change the formula to 
    # -a+c * (capacity_A) + -b+c (capacity_B) - target = 0  or
    # -a+c * (capacity_A) + -b+c (capacity_B) = target
    # because c is a float, we can just treat a, b as the integer part of a number
    # and check if their decimal parts are equal
    # math solution said it's equivalent to if target % gcd(x,y) = 0
    # but i haven't figure that out yet

    #BFS approach
    # brute force each possible operation until we cannot possibly return the target
    # end state would be 
    # 1. both jugs are filled,
    # 2. one filled one empty,
    # 3. both empty 
    # (meaning we have returned to the initial state)

    # for BFS we need a queue
    graph = deque([]) # start with empty queue
    initial = (0, 0) # this is the initial operation
    visited = {(0,0)} # a set of visited nodes

    # concept: for each possible operation, we do the oprn
    # and check all the states possoible after
    # and then put those states into the queue (BFS core logic)
    # once we hit a end state, we simply skip that state
    # once the deque is empty and we still don't hit the target
    # we return False
    graph.append((0,0))
    graph.append((x,0))
    graph.append((0,y))
    end_states = {(0,0), (x,y), (x, 0), (0, y)} # because we already have those as initial states
    # repeated occurance means we are back to the initial states

    iteration_states = deque([]) # for storing iteration states
    while graph:
        node = graph.popleft()

        # check if we have success
        if (node[0] + node[1] == target): return True

        # examine all possible operation and their effects
        # empty one jug
        iteration_states.append((0, node[1]))
        # empty another jug
        iteration_states.append((node[0], 0))
        # fill one jug to full
        iteration_states.append((x, node[1]))
        # fill another jug to full
        iteration_states.append((node[0], y))
        # transfer from one jug to another jug
        pour = min(node[0], (y - node[1])) # either pour all or the remaining capacity of jug B
        iteration_states.append((node[0] - pour, node[1] + pour))

        # transfer from another jug to one jug
        pour = min((x - node[0]), node[1]) # either pour all or the remaining capacity of jug A
        iteration_states.append((node[0] + pour, node[1] - pour))

        for state in iteration_states:
            if state not in visited and state not in end_states and state not in graph:
                visited.add(state)
                graph.append(state)
        iteration_states.clear() # clear the iteration states


    return False # if the deque is empty and we don't find any pair target

if __name__ == "__main__":
    testCases = [(1,2,3), (3,5,4), (2,6,5)]
    for case in testCases:
        print(canMeasureWater(case[0], case[1], case[2]))



