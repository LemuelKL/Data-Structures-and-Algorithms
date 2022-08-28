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
    if (k < 1):
        return 0

    fill = 0
    for p in str:
        if p == "(":
            fill += 1
        elif p == ")":
            fill -= 1
        if fill < 0 or fill - 1 > k:
            return 0

    fill = 0;
    answer = 1;
    for i in range(1, n):
        if (str[i] == '('):
            fill += 1
        elif (str[i] == ')'):
            fill -= 1
        
        if (fill < 0):
            return answer
        if (fill + 1 <= k):
            answer += 1
        elif (fill == k):
            answer = 0
    
    return answer;


print(solution(6, "()()()", 2))
print(solution(6, "(()())", 3))
print(solution(6, "((()))", 2))
print(solution(6, "(())()", 1))

