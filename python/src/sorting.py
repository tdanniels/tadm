from collections import deque
import timeit


def selection_sort(l: list):
    for i in range(len(l)):
        min_ = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_]:
                min_ = j
        l[i], l[min_] = l[min_], l[i]


def insertion_sort(l: list):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1


def heapsort(l: list):
    # [heap_len, heap]
    q = [0, l]

    def pq_parent(i):
        if i == 0:
            return None
        return (i - 1) // 2

    def pq_first_child(i):
        return 2 * i + 1

    def pq_insert(q, v):
        q[0] += 1
        q[1][q[0] - 1] = v
        bubble_up(q, q[0] - 1)

    def bubble_up(q, i):
        parent = pq_parent(i)
        if parent is not None and q[1][parent] < q[1][i]:
            q[1][i], q[1][parent] = q[1][parent], q[1][i]
            bubble_up(q, parent)

    def make_maxheap(q, l, n):
        for i in range(n):
            pq_insert(q, l[i])

    def extract_max(q):
        if q[0] == 0:
            raise ValueError("Tried to extract max from an empty queue")
        max_ = q[1][0]
        q[1][0] = q[1][q[0] - 1]
        q[0] -= 1
        bubble_down(q, 0)
        return max_

    def bubble_down(q, i):
        c = pq_first_child(i)
        max_index = i

        for j in (0, 1):
            if c + j <= q[0] - 1 and q[1][max_index] < q[1][c + j]:
                max_index = c + j

        if max_index != i:
            q[1][i], q[1][max_index] = q[1][max_index], q[1][i]
            bubble_down(q, max_index)

    make_maxheap(q, l, len(l))
    for i in reversed(range(len(l))):
        l[i] = extract_max(q)


def mergesort(l: list):
    def _mergesort(l, low, high):
        if low < high:
            middle = (low + high) // 2
            _mergesort(l, low, middle)
            _mergesort(l, middle + 1, high)
            merge(l, low, middle, high)

    def merge(l, low, middle, high):
        buf1 = deque()
        buf2 = deque()

        for i in range(low, middle + 1):
            buf1.append(l[i])
        for i in range(middle + 1, high + 1):
            buf2.append(l[i])

        i = low
        while buf1 and buf2:
            if buf1[0] <= buf2[0]:
                l[i] = buf1.popleft()
            else:
                l[i] = buf2.popleft()
            i += 1

        while buf1:
            l[i] = buf1.popleft()
            i += 1
        while buf2:
            l[i] = buf2.popleft()
            i += 1

    _mergesort(l, 0, len(l) - 1)


def quicksort(l: list):
    def _quicksort(l, low, high):
        if low < high:
            p = partition(l, low, high)
            _quicksort(l, low, p - 1)
            _quicksort(l, p + 1, high)

    def partition(l, low, high):
        p = high
        firsthigh = low
        for i in range(low, high):
            if l[i] < l[p]:
                l[i], l[firsthigh] = l[firsthigh], l[i]
                firsthigh += 1
        l[p], l[firsthigh] = l[firsthigh], l[p]

        return firsthigh

    _quicksort(l, 0, len(l) - 1)


def unique_words(ls: list[str]) -> list[str]:
    """Assumes `ls` is sorted."""
    out = []
    prev = None
    for s in ls:
        if s == prev:
            continue
        prev = s
        out.append(s)
    return out


def tokenize(corpus: str) -> list[str]:
    out = []
    for s in corpus.split():
        if not s.isalpha():
            continue
        s = s.lower()
        out.append(s)
    return out


def load_corpus(filename: str) -> str:
    with open(filename) as f:
        corpus = f.read()
        return corpus


if __name__ == "__main__":
    corpus = load_corpus("./src/solutions.md")
    tokens = tokenize(corpus)
    print(f"len(tokens) = {len(tokens)}")
    outputs = []
    baselinetime = 0

    for i, sort in enumerate(
        (
            list.sort,
            selection_sort,
            insertion_sort,
            heapsort,
            mergesort,
            quicksort,
        )
    ):
        tokens_copy = tokens[:]
        start = timeit.default_timer()
        sort(tokens_copy)
        stop = timeit.default_timer()
        tokens_unique = unique_words(tokens_copy)
        outputs.append(tokens_unique)
        if len(outputs) > 1:
            assert outputs[-2] == outputs[-1]
        else:
            print(f"Sample output: {outputs[0][:10]}")
        deltatime = stop - start
        if i == 0:
            baselinetime = deltatime
        print(f"Sort function '{sort.__name__}' took {deltatime} seconds: ", end="")
        print(f"{deltatime / baselinetime:.3f}x baseline.")
