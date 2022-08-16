# O(2^n) time
# O(n) space
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# O(n) time
# O(n) space
def fib_fast(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_fast(n - 1, memo) + fib_fast(n - 2, memo)
        memo[n] = result
        return result


print(fib_fast(99))
