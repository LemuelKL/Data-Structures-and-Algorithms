# 2021-2022
# COMP2119A
# Assignment 1
# Task B

# S_{i + 1} = reverse(invert(S_i)) + "0" + S_i

S1 = "1"
S2 = "001"
S3 = "0110001"
S4 = "011100100110001"

# Given two integers n > 0 and k > 0, k <= 2^n -1, find the kth bit in S_n.

S5 = "0111001101100010011100100110001"

memory = {
    '00': '0011',
    '01': '0001',
    '10': '1011',
    '11': '1001'
}

def kth_bit(n, k):
    now = "01"
    l = 2 ** n - 1
    mid = l

    while l > 2:
        mid //= 2
        print("L:", l, "Mid:", mid)
        if k <= mid:
            # print("Left")
            now = memory[now][0:2]
        else:
            # print("Right")
            now = memory[now][2:]
            k -= mid + 1
        
        l //= 2

    # print(now, k)
    return now[k]

# print(kth_bit(42069, 2049))
print(kth_bit(1997, 444))