s = [x for x in range(1000)]


def main():
    push_cursor = 0
    pop_cursor = -1
    while True:
        cmd = input().split()
        if cmd[0] == 'push':
            s[push_cursor] = cmd[1]
            push_cursor += 1
            pop_cursor = push_cursor - 1
        elif cmd[0] == "pop":
            if pop_cursor == -1:
                print("empty")
                return
            else:
                print(s[pop_cursor])
                pop_cursor -= 1
                push_cursor = pop_cursor + 1


if __name__ == "__main__":
    main()
