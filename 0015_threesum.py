from typing import *
def threeSum(nums: List[int]) -> List[List[int]]:
    list_res = []
    #null check, typing is checked before input
    if len(nums) < 3: return [] #triplet must have at least 3 elements

    sorted_in = sorted(nums)
    # sorted, that means
    # when left +1, you will always get a bigger number
    # when right -1 you will always get a smaller number

    for i in range(len(sorted_in)-1):
        #skip the later dupliactes, use the first occurance, index 0 will never be a duplicate 
        if i > 0 and sorted_in[i] == sorted_in[i-1]: continue

        #use two pointers
        left = i + 1 # first element index, we only search to the right of i because previous elements are all checked
        right = len(sorted_in) - 1 # last element index
        matching = -1 * sorted_in[i]
        # thinking: focus on one element at a time, find pair that adds up to -(element)
        # skip duplicate after the search
        while left < right: # while the two pointers are not overlapping
            candidate = sorted_in[left] + sorted_in[right]
            if candidate == matching: # means we find a pair
                list_res.append([sorted_in[i], sorted_in[left], sorted_in[right]]) #record the triplet
                
                # move forward
                left += 1
                right -= 1
                #skip duplicates, while the left and right don't overlap
                while left < right and sorted_in[left] == sorted_in[left -1]: left += 1
                while left < right and sorted_in[right] == sorted_in[right +1]: right -= 1

            elif candidate < matching: # means we need a bigger pair
                left += 1 # left go forward    
            else: #means candidate > machting, we need a smaller pair
                right -= 1



    return list_res
    

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))