from typing import *
from collections import *

"""
examples
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

stack
overall:
read through the string, store open brackets throughout the process
whenever we encouter a closed bracket, we push the repeated string
into the result (tbd)

step1: 
read the string char by char

right after a number there's always a '['
set of numbers {1-9}
set of char {']'}

step2:
once we hit the closing ]
we multiply whatever the string is stored and contactate
to the result

"""
def decodeString(s: str) -> str:
    # edge cases / impossible cases
    if not s: return ""

    stk = [] # list as a stack

    # normal cases
    #read the string into the stack    
    for char in s:
        if char != ']': # as long as it's not a closing bracket
            stk.append(char) # add the char into the stack
        else: 
            # once we hit the first closing bracket,
            # we process the loop
            # and then push it back to the stack
            # ----
            # pop everything from stack until an '['
            temp = ""
            while stk and stk[-1] != '[': 
                #while the element on top of the stack is not '[' 
                temp = stk.pop() + temp
            stk.pop() # pop the last '['

            mult = 0
            digit = 0 # represents decimal location
            while stk and stk[-1].isdigit():
                #we don't update the digit here because 1 is 10^0
                mult = mult + (10 ** digit) * int(stk.pop())
                digit += 1 # start with x1, then x10, then x100,...
            temp *= mult
            #push the string back to the stack
            stk.append(temp)
            digit = 0 # reset the digit
    
    return "".join(stk)

if __name__ == "__main__":
    s = "3[a]2[bc]"
    print(decodeString(s))
