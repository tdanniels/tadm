# start snippet find-k
def find_k(l, begin, end):
    i = 1
    if begin + i > end:
        return 0
    while True:
        if l[begin] > l[begin + i]:
            if i == 1:
                return begin + i
            else:
                return find_k(l, begin + i // 2, begin + i)
        else:
            if i == end - begin:
                return 0
            i = min(i * 2, end - begin)
    # end snippet find-k
