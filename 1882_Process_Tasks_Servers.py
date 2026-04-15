from typing import *
from collections import *
import heapq

def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    busy = [] # heap for busy servers, hold tuple (free_time, w, i)
    free = [] # heap for free servers, hold tuple (w,i), w has priority in comparison
    ans = [0] * len(tasks) # result array, will overwrite later
    # rules:
    # server: index and values at index are weights

    # tasks: index are task order and values at index are time needed to complete the task
    # at second A, task[A] will be executed, if no free server is available, we'll
    # wait until the next server is free, in case of multiple servers are free at that time
    # we pick the server with lowest weight, if tie, then server with lowest index

    # goal: build an array ans[], such that ans[j] would be the index of the server for jth task

    # edge cases / impossible cases
    if (not tasks) or (not servers): # if either tasks or servers are empty
        return [] # ans would be an empty list, not None!!!
    elif len(servers) == 1: # if there's only one server
        return ans # ans would be default value (all the same server)
    
    # normal cases

    # fill all servers to free, ordered by weight, and then index
    for i, w in enumerate(servers):
        heapq.heappush(free, (w,i)) # noted that w is in front of i because of priority
    
    time_pointer = 0 # points to the current time of assigning process
    # main loop: push task to free servers, one by one
    for index, time_needed in enumerate(tasks): # for each task in task, we pop the right server to them, if no server then we wait
        free_available_server(busy, index, free) # release all availabe server at time <index>
        if not free: 
            # if no server is free after the release, 
            # that means we have to wait until the first server is freed
            next_time = busy[0][0] # jump to the second of the wait time of the first busy element
            time_pointer = busy[0][0] # no assignment is happening until time_pointer time
            free_available_server(busy, next_time, free) # free again, guaranteed at least one server would be available
            pop_free_and_push_busy(ans, free, busy, time_needed, index, next_time) 
            # in the wait case, the starting time of the task is next_time
        elif time_pointer > index: # in case of previous delay for waiting a free server
            pop_free_and_push_busy(ans, free, busy, time_needed, index, time_pointer)
        else: # some server is free at the time of index
            pop_free_and_push_busy(ans, free, busy, time_needed, index)

    return ans

def pop_free_and_push_busy(ans, free, busy, time_needed, index, next_time=0):
    w, ans[index] = heapq.heappop(free) # get the available server
    # what ever the server assign to
    # the index would be our answer in ans[]
    # the new finish time would be current time(index) + finish_time (time needed to finish)
    # in the wait case, the starting time is not Index, but next_time
    starting_time = index if index >= next_time else next_time
    heapq.heappush(busy, ((time_needed+starting_time), w, ans[index])) # push the server back to busy

def free_available_server(busy, time_to_free, free): # helper function
    # free all server that should be available by time
    while busy and busy[0][0] <= time_to_free: # represent unit time
        # this while loop checks for :
        # if the busy heap has some element, and for all element that would be free by the 
        # at time_to_free, free the servers, so we can pick the correct server
        free_time, w, i = heapq.heappop(busy)
        heapq.heappush(free, (w,i)) # push it back to free heap  

if __name__ == "__main__":
    servers = [3,3,2]
    tasks = [1,2,3,2,1,2]
    #edge cases
    Servers = [1, 2, 3]
    Tasks = [5, 4, 3, 1, 2] #Answer should be [0, 1, 2, 0, 1]
    print(assignTasks(Servers, Tasks))