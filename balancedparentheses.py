# A parentheses string s contains just the characters ‘(’ and ‘)’. The string matches an
# operation sequence starting from an empty stack: ‘(’ stands for ‘push’ operation, and ‘)’
# stands for ‘pop’ operation. A parentheses string is valid if open brackets are closed in
# the correct order, which has equal numbers of ‘(’ and ‘)’, and there is no underflow when
# executing the matched operation sequence on the stack.

# Now, we delete the first character, which is ‘(’, and then insert the deleted ‘(’ into some
# position. Observe that if there are n symbols in the original string, then the first character
# has n possible insertion positions (including its original position).

# After the insertion, if the new parentheses string satisfies the following properties, we call
# it a valid insertion. Given a stack of maximum capacity k,

# 1. there is no underflow when executing the operation sequence. (Underflow happens when
# we try to pop an item from an empty stack.)
# 2. there is no overflow when executing the operation sequence. (Overflow happens when
# we try to push an item to a stack of size equal to its maximum capacity.)

# Assume the given stack is empty at first. Output the number of positions where insertion
# is valid. Your algorithm must run in O(n) time, where n is the length of the parentheses
# string.


def solution(n, str, k):
    idx = 0
    fill = 0
    num_underflow = 0
    check_underflow = True
    num_overflow = 0
    check_overflow = True

    while idx < n:
        p = str[idx]
        if p == '(':
            fill += 1
        else:
            fill -= 1
        # print(p, fill)
        if (check_underflow and fill == 0):
            num_underflow = n - idx
            check_underflow = False
        if (check_overflow and fill > k):
            num_overflow = idx + 1
            check_overflow = False
        
        idx += 1
    
    # print(num_underflow, num_overflow)
    return n - num_underflow - num_overflow


print(solution(6, '()()()', 2))
print(solution(6, '(()())', 3))
print(solution(6, '((()))', 2))
print(solution(6, '(())()', 1))

# Key observation
# No. of underflow = no. of parentheses at and after first encounter of 0
# No. of overflow = no. of parentheses at and before first encounter of fill > k
