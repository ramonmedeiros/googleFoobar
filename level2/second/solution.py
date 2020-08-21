def solution(n, b):
    ids = []
    # 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
    k = len(n)
    while n not in ids:
        
        # save id
        ids.append(n)

        # 2) Define x and y as integers of length k.  x has the digits of n in descending order
        # and y has the digits of n in ascending order
        y  = "".join(sorted(list(n)))
        x = "".join(sorted(list(n), reverse=True))

        # 3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
        if b == 10:
            z = str(int(x) - int(y))
        else:
            z = baseToDecimal(x, b) - baseToDecimal(y, b)
            z = decimalToBase(z, b)

        z = (k - len(z))*'0' + z

        # 4) Assign n = z to get the next minion ID, and go back to step 2
        n = z
    return len(ids) - ids.index(n)


def decimalToBase(number, base):
    baseNumber = ""
    while number > 0:
        mod = int(number % base)
        if mod < 10:
            baseNumber += str(mod)
        else:
            baseNumber += chr(ord('A')+mod-10)
        number //= base
    baseNumber = baseNumber[::-1]
    return baseNumber

def baseToDecimal(number, base):
  n = 0
  for d in number:
    n = base * n + int(d)
  return n


assert solution('1211', 10) == 1
assert solution('210022', 3) == 3
