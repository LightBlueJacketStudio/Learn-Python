def longestPalindrome(s: str) -> str:
    #prepare the modified string
    # so that each space in the middle can be center as well
    t = "#" + "#".join(s) + "#" 
    # maintain the center and the right edge of the right most palidrome
    
    pass






if __name__ == "__main__":

    s = "babad"
    print(longestPalindrome(s))
