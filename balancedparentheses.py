def solution(str):
    stack = []
    for char in str:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()


    if len(stack) == 0:
        return True
    return False

print(solution('({[}]'))
print(solution('()[]{}'))
print(solution('([]{}'))
print(solution('([]{})'))
print(solution('([(([{}]))]{()})'))
print(solution('([(([{}]))]{([)]})'))
