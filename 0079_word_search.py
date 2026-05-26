
""" Solution
class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

"""
# time complexity: O(m * n * 4^L) 
# m = number of rows
# n = number of columns
# L = length of word

# space complexity is the same

from typing import *
from collections import *

# given a board, M x N

def exist(board, word):
    # edge cases / impossible cases
    if not board: return False # empty board passed in
    elif not word: return True # the word is empty, any board would suffice

    visited = set()

    # normal cases

    # helper function for DFS
    # input would be the starting index and the next char 
    # (denoted by the index of the word)
    # since word is a string
    def search(i, j, word_index):
        # base case (True)
        if word_index == len(word): # we have reached the end of word
            return True
        # base case (False)
        # out of bound check should be put first
        if (
            i < 0 or j < 0 # invalid index
            or i >= len(board) or j >= len(board [0]) # out of bound
            or (i,j) in visited # already visited
            or board[i][j] != word[word_index] # not the word we are looking for
            ):
            return False
        

        # subsequent recurrsion
        
        # add the tuple into visited
        visited.append((i,j))

        # search in all possible directions
        found = (
            search(i+1, j, word_index +1)
            or search(i, j+1, word_index +1)
            or search(i-1, j, word_index +1)
            or search(i, j-1, word_index +1)
        )

        # backtracking the cell, since now we finished searching this element in board
        visited.pop()

        return found

    # for every element we do DFS search
    for row in range(len(board)):
        for cloumn in range(len(board[0])):
            visited = [] # clear the visited
            if search(row, cloumn, 0):
                return True

    return False # mean we didn't find the word
            


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    board = [["a"]]
    word = "a"

    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    print(exist(board, word))
