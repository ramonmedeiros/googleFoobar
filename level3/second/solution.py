
def solution(mach, facula):
    """
    Every Mach -> retrieves sync unit Facula. For every mach, facula is created
    Every Facula -> creates Mach

    What is a sync unit?
    """
    mach = long(mach)
    facula = long(facula)
    cycles = 0

    while mach!= 1 or facula != 1:
        if mach == 1 or facula == 1:
            if mach == 1:
                cycles += facula - 1
            if facula == 1:
                cycles += mach- 1
            break

        if mach < facula:
            if mach == 0:
                return "impossible"
            cycles += facula / mach
            facula %= mach
        else:
            if facula == 0:
                return "impossible"
            cycles += mach / facula
            mach %= facula
    return str(cycles)

assert solution('2', '1') == "1"
assert solution('4', '7') == "4"
assert solution('2', '4') == "impossible"
