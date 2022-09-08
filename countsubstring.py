def count(s):
    cnt = 0
    idx = 0
    for l in s:
        if l == "1":
            for r in s[idx + 1 :]:
                if r == "1":
                    cnt += 1
        idx += 1

    return cnt


def count_fast(s):
    cnt = 0
    for l in s:
        if l == "1":
            cnt += 1

    return cnt * (cnt - 1) // 2


if __name__ == "__main__":
    print(count("00100101"))
    print(count("001010111010001"))

    print(count_fast("00100101"))
    print(count_fast("001010111010001"))
