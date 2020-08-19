
# TODO: Got only 50% on this one. In README, says that x and y can be from 1 to 100.00
# Maybe add big numbers support next time
def solution(x, y):
    # x is line, y is column
    rowValue = calculateRow(y)

    res = rowValue
    s = y + 1
    for i in range(x-1):
        res += s
        s += 1
    return str(res)


def calculateRow(row):
    res = 1
    s = 1
    for i in range(row-1):
        res += s
        s += 1
    return res


assert solution(1, 1) == "1"
assert solution(3, 2) == "9"
assert solution(2, 3) == "8"
assert solution(5, 10) == "96"

