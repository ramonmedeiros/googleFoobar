def solution(n):
    n = long(n)
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            minus = (n - 1) & ~(n - 1 - 1)
            plus = (n + 1) & ~(n + 1 - 1)

            if minus > plus or minus == n - 1:
                n -= 1
            else:
                n += 1
        counter += 1
    return counter

assert solution("15") == 5
assert solution("13") == 5
assert solution("4") == 2
assert solution("2") == 1
assert solution("1") == 0

