from collections import deque

import copy
import random
import timeit
import unittest

import bst
import combinatorial
import graph
import linkedlist
import sorting

import l02_01
import l02_03
import l04_01
import p01_01
import p01_03
import q01_27
import q03_01
import q03_09
import q03_17
import q03_29
import q04_31
import q04_35
import q04_45


class TestQ01_27(unittest.TestCase):
    def test(self):
        S = [1, 2, 3, 4, 5]
        k = 3
        l = 2
        self.assertTrue(q01_27.check_tickets([[1, 2, 3], [1, 4, 5]], S, k, l))
        self.assertFalse(q01_27.check_tickets([[1, 2, 3], [1, 2, 4]], S, k, l))

        gen = q01_27.gen_tickets(S, k, l)
        self.assertTrue(q01_27.check_tickets(gen, S, k, l))
        self.assertEqual(len(gen), 2)

        S = list(range(1, 11))
        k = 6
        l = 3
        gen = q01_27.gen_tickets(S, k, l)
        self.assertTrue(q01_27.check_tickets(gen, S, k, l))

        S = list(range(1, 16))
        k = 6
        l = 3
        self.assertTrue(
            q01_27.check_tickets(
                [
                    [2, 4, 8, 10, 13, 14],
                    [4, 5, 7, 8, 12, 15],
                    [1, 2, 3, 6, 11, 13],
                    [3, 5, 6, 9, 10, 15],
                    [1, 7, 9, 11, 12, 14],
                ],
                S,
                k,
                l,
            )
        )
        self.assertFalse(
            q01_27.check_tickets(
                [
                    [2, 4, 8, 10, 13, 14],
                    [4, 5, 7, 8, 12, 15],
                    [1, 2, 3, 6, 11, 13],
                    [3, 5, 6, 9, 10, 15],
                ],
                S,
                k,
                l,
            )
        )


class TestQ03_01(unittest.TestCase):
    def test(self):
        self.assertTrue(q03_01.balanced_parens("((())())()"))
        self.assertTrue(q03_01.balanced_parens("((())(()(())))"))
        self.assertFalse(q03_01.balanced_parens(")()("))
        self.assertFalse(q03_01.balanced_parens("())"))
        self.assertFalse(q03_01.balanced_parens("((("))
        self.assertFalse(q03_01.balanced_parens("()(()"))


class TestQ03_09(unittest.TestCase):
    def test(self):
        s1 = bst.from_list([[1], 2, [3]])
        s2 = bst.from_list([[4], 5, [6]])
        s3 = [[[1], 2], 3, [[4], 5, [6]]]
        con = q03_09.concatenate(s1, s2)
        self.assertEqual(con.to_list(), s3)


class TestQ03_17(unittest.TestCase):
    def test(self):
        text = "ETA: tee ate"
        shift = 7
        ao = ord("a")
        zo = ord("z")
        cipher = {
            chr(u): chr(v)
            for (u, v) in zip(
                range(ao, zo + 1),
                map(lambda x: ((x - ao + shift) % 26) + ao, range(ao, zo + 1)),
            )
        }
        ctext = q03_17.caesar(text, cipher)
        decipher = q03_17.frequency_analysis(ctext)
        decrypted = q03_17.caesar(ctext, decipher)
        self.assertEqual(
            decrypted,
            "".join([c.lower() if c.isalpha() and c.isascii() else c for c in text]),
        )
        pass


class TestQ03_29(unittest.TestCase):
    def test(self):
        text = """The Free State of Dorimare was a very small country, but,
        seeing that it was bounded on the south by the sea and on the north and
        east by mountains, while its centre consisted of a rich plain, watered
        by two rivers, a considerable variety of scenery and vegetation was to
        be found within its borders. Indeed, towards the west, in striking
        contrast with the pastoral sobriety of the central plain, the aspect of
        the country became, if not tropical, at any rate distinctly exotic. Nor
        was this to be wondered at, perhaps; for beyond the Debatable Hills
        (the boundary of Dorimare in the west) lay Fairyland. There had,
        however, been no intercourse between the two countries for many
        centuries."""

        self.assertEqual(q03_29.max_bigram(text), ("on", "the", 2))


class TestQ04_31(unittest.TestCase):
    def test(self):
        for qlen, k in [
            (1, 0),
            (2, 0),
            (2, 1),
            (4, 1),
            (4, 2),
            (4, 3),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
            (100, 1),
            (101, 48),
            (101, 49),
            (103, 96),
        ]:
            q = deque(range(qlen))
            q.rotate(k)
            k_ = q04_31.find_k(q, 0, len(q) - 1)
            self.assertEqual(k_, k)


class TestQ04_35(unittest.TestCase):
    def test(self):
        for m, sought, loc in [
            ([[1]], 1, (0, 0)),
            ([[1]], 0, None),
            ([[1, 2, 2], [2, 2, 2], [2, 2, 2]], 1, (0, 0)),
            ([[-1, 0, 1], [1, 1, 1], [1, 1, 1]], 0, (0, 1)),
            ([[-1, 1, 1], [0, 1, 1], [2, 3, 4]], 0, (1, 0)),
            ([[1, 1, 2], [1, 1, 3], [1, 1, 4]], 2, (0, 2)),
            ([[1, 2, 2], [2, 2, 2], [3, 4, 4]], 3, (2, 0)),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 2]], 2, (2, 2)),
            ([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], -1, None),
            ([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 4, (1, 0)),
        ]:
            self.assertEqual(
                q04_35.binary_search_2d(m, sought, (0, len(m) - 1), (0, len(m[0]) - 1)),
                loc,
            )
            self.assertEqual(
                q04_35.saddleback(m, sought),
                loc,
            )

    @unittest.skip("slow")
    def test_bigmatrix(self):
        random.seed(314159)

        n = 1000
        sought = 1001
        m = [[random.randrange(-1000, 1000, 2) for _ in range(n)] for _ in range(n)]
        m[n // 2][n // 2] = sought
        for row in m:
            row.sort()
        for j in range(n):
            col = [m[row][j] for row in range(n)]
            col.sort()
            for i in range(n):
                m[i][j] = col[i]

        start = timeit.default_timer()
        floc = q04_35.binary_search_2d(m, sought, (0, len(m) - 1), (0, len(m[0]) - 1))
        end = timeit.default_timer()
        print(f"binary_search_2d took {end-start} seconds")

        start = timeit.default_timer()
        sloc = q04_35.saddleback(m, sought)
        end = timeit.default_timer()
        print(f"saddleback took {end-start} seconds")

        start = timeit.default_timer()
        for i in range(n):
            for j in range(n):
                if m[i][j] == sought:
                    loc = (i, j)
                    break
        end = timeit.default_timer()
        print(f"naive matrix search took {end-start} seconds")

        self.assertEqual(floc, loc)
        self.assertEqual(sloc, loc)


class TestQ04_45(unittest.TestCase):
    def test(self):
        for w1, w2, w3, s in (
            [[0, 4, 7], [1, 8], [5, 9], (7, 9)],
            [[1, 4, 5], [2, 7, 8], [3, 9, 16], (1, 3)],
            [[1, 10], [2, 20], [3, 30], (1, 3)],
            [[1, 9, 27], [6, 10, 19], [8, 12, 14], (8, 10)],
            [[1, 4, 11, 27], [3, 6, 10, 19], [5, 8, 12, 14], (3, 5)],
            [[1, 4, 5], [3, 9, 10], [2, 6, 15], (1, 3)],
        ):
            self.assertEqual(q04_45.closest3(w1, w2, w3), s)


class TestP01_01(unittest.TestCase):
    def test(self):
        self.assertEqual(p01_01.solve(1, 10), "1 10 20")
        self.assertEqual(p01_01.solve(100, 200), "100 200 125")
        self.assertEqual(p01_01.solve(201, 210), "201 210 89")
        self.assertEqual(p01_01.solve(900, 1000), "900 1000 174")
        self.assertEqual(p01_01.solve(1000, 900), "1000 900 174")
        # Worst case input:
        self.assertEqual(p01_01.solve(1, 9999), "1 9999 262")


class TestP01_03(unittest.TestCase):
    def test(self):
        inp = deque(
            [
                "1",
                "",
                "3",
                "John Doe",
                "Jane Smith",
                "Sirhan Sirhan",
                "1 2 3",
                "2 1 3",
                "2 3 1",
                "1 2 3",
                "3 1 2",
            ]
        )
        self.assertEqual(p01_03.solve(p01_03.parse(inp)), ["John Doe"])

        inp = deque(
            [
                "2",
                "",
                "3",
                "John Doe",
                "Jane Smith",
                "Sirhan Sirhan",
                "1 2 3",
                "2 1 3",
                "2 3 1",
                "1 2 3",
                "3 1 2",
                "",
                "2",
                "a",
                "b",
                "1 2",
                "2 1",
            ]
        )
        self.assertEqual(p01_03.solve(p01_03.parse(inp)), ["John Doe", "", "a", "b"])


class TestL02_01(unittest.TestCase):
    def test(self):
        s = l02_01.Solution()

        for d, k, soln in [
            ("52660469", 2, "260469"),
            ("1234", 3, "1"),
            ("1432219", 3, "1219"),
            ("111999", 3, "111"),
            ("1110009", 3, "9"),
            ("102030", 3, "0"),
            ("0", 1, "0"),
            ("12343475437852347858912364501948465", 10, "1232347858912364501948465"),
            (
                "949463029467549391366849402029384756574651343557689700",
                15,
                "21366849402029384756574651343557689700",
            ),
            ("1" * 5 * 10**3 + "0" * 5 * 10**3, 10**4, "0"),
        ]:
            rkd = s.removeKdigits(d, k)
            self.assertEqual(rkd, soln)


class TestL02_03(unittest.TestCase):
    def test(self):
        s = l02_03.Solution()
        self.assertEqual(
            sorted([sorted(l) for l in s.fourSum([1, 0, -1, 0, -2, 2], 0)]),
            sorted(sorted(l) for l in [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        )
        self.assertEqual(s.fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])


class TestL04_01(unittest.TestCase):
    def test(self):
        head = l04_01.ListNode(4)
        head.next = l04_01.ListNode(2)
        head.next.next = l04_01.ListNode(1)
        head.next.next.next = l04_01.ListNode(3)

        s = l04_01.Solution()
        newhead = s.sortList(head)
        print(newhead.val)
        print(newhead.next.val)
        print(newhead.next.next.val)
        print(newhead.next.next.next.val)

        self.assertEqual(newhead.val, 1)
        self.assertEqual(newhead.next.val, 2)
        self.assertEqual(newhead.next.next.val, 3)
        self.assertEqual(newhead.next.next.next.val, 4)


class TestBST(unittest.TestCase):
    def test_list(self):
        l1 = [[1], 2, [3]]
        l2 = [[1], 2, [4]]
        self.assertEqual(bst.from_list(l1).to_list(), l1)
        self.assertNotEqual(bst.from_list(l1).to_list(), l2)

    def test_eq(self):
        l1 = [[1], 2, [3]]
        t1 = bst.from_list(l1)
        t11 = bst.from_list(l1)
        l2 = [[1], 2, [4]]
        t2 = bst.from_list(l2)
        self.assertTrue(t1 == t11)
        self.assertFalse(t1 == t2)


class TestCombinatorial(unittest.TestCase):
    def test_derangements(self):
        for n, d in [[1, []], [2, [[2, 1]]], [3, [[2, 3, 1], [3, 1, 2]]]]:
            self.assertEqual(combinatorial.derangements(n), d)

    def test_graph_isomorphism(self):
        for g, h, iso in (
            (
                [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                True,
            ),
            (
                [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                [[0, 1, 1], [1, 0, 1], [0, 1, 0]],
                False,
            ),
            (
                [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]],
                [[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]],
                True,
            ),
            (
                [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]],
                [[0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 1, 1, 0]],
                False,
            ),
        ):
            self.assertEqual(combinatorial.graph_isomorphism(g, h), iso)

    @unittest.skip("slow")
    def test_graph_isomorphism_big(self):
        random.seed(314159)
        r1 = graph.random_adj_matrix(100)
        r2 = copy.deepcopy(r1)
        r2[70][75] ^= 1
        r2[75][70] ^= 1
        for g, h, iso in (
            (r1, r1, True),
            (r1, r2, False),
        ):
            self.assertEqual(combinatorial.graph_isomorphism(g, h), iso)


class TestGraph(unittest.TestCase):
    def test_floyd_warshall(self):
        g = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        spm = graph.floyd_warshall(g, False)
        self.assertEqual([[2, 1, 1], [1, 2, 1], [1, 1, 2]], spm)
        spm = graph.floyd_warshall(g)
        self.assertEqual([[0, 1, 1], [1, 0, 1], [1, 1, 0]], spm)

    def test_random_adj_matrix(self):
        random.seed(314159)
        n = 7
        m = graph.random_adj_matrix(n)
        for i in range(n):
            for j in range(n):
                self.assertEqual(m[i][j], m[j][i])

    def test_adj_matrix_multiply(self):
        m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(graph.adj_matrix_multiply(m1, m1), m1)
        m2 = [[1, 3, 1], [2, 1, -1], [5, 0, 1]]
        m3 = [[0, 2, 6], [-3, 2, 0], [3, 1, 4]]
        self.assertEqual(
            graph.adj_matrix_multiply(m2, m3), [[-6, 9, 10], [-6, 5, 8], [3, 11, 34]]
        )


class TestLinkedList(unittest.TestCase):
    def test(self):
        ls = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
        for l in ls:
            self.assertEqual(linkedlist.LinkedList.from_list(l).to_list(), l)
            self.assertEqual(
                linkedlist.LinkedList.from_list(l).reverse().to_list(),
                list(reversed(l)),
            )
            self.assertEqual(
                linkedlist.LinkedList.from_list(l).reverse_nr().to_list(),
                list(reversed(l)),
            )

    def test_loop(self):
        ls = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
        for l in ls:
            self.assertFalse(linkedlist.LinkedList.from_list(l).has_loop())

        loop = linkedlist.LinkedList(1, None)
        self.assertFalse(loop.has_loop())
        loop.append(linkedlist.LinkedList(2, None))
        self.assertFalse(loop.has_loop())
        loop.append(linkedlist.LinkedList(3, loop))
        self.assertTrue(loop.has_loop())


class TestSorting(unittest.TestCase):
    def test(self):
        random.seed(314159)
        seqs = [
            [],
            [1],
            [1, 2],
            [2, 1],
            [1, 2, 3],
            [2, 1, 3],
            [3, 2, 1],
            list(range(50)),
            list(range(10)) * 10,
        ]
        random.shuffle(seqs[-2])
        random.shuffle(seqs[-1])

        baselines = []
        for i, sort in enumerate(
            (
                list.sort,
                sorting.selection_sort,
                sorting.insertion_sort,
                sorting.heapsort,
                sorting.mergesort,
                sorting.quicksort,
            )
        ):
            for j, s in enumerate(seqs):
                s_copy = s[:]
                sort(s_copy)
                if i == 0:
                    baselines.append(s_copy)
                else:
                    self.assertEqual(s_copy, baselines[j])


if __name__ == "__main__":
    unittest.main()
