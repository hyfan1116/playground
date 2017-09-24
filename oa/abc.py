# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    if 'A' not in S and 'C' not in S:
        return S
    else:
        result = ""
        for c in S:
            if c != 'B':
                current = c
                break  
        for c in S:
            if c == 'B' or c == current:
                pass
            else:
                result = result+current
                current = c
        result = result+current
        return result
    pass