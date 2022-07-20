from collections import deque

import importlib
import unittest


q1_27 = importlib.import_module("src.1-27")
p1_1 = importlib.import_module("src.p1-1")
p1_3 = importlib.import_module("src.p1-3")
l2_1 = importlib.import_module("src.l2-1")
l2_3 = importlib.import_module("src.l2-3")


class Test1_27(unittest.TestCase):
    def test(self):
        S = [1, 2, 3, 4, 5]
        k = 3
        l = 2
        self.assertTrue(q1_27.check_tickets([[1, 2, 3], [1, 4, 5]], S, k, l))
        self.assertFalse(q1_27.check_tickets([[1, 2, 3], [1, 2, 4]], S, k, l))

        gen = q1_27.gen_tickets(S, k, l)
        self.assertTrue(q1_27.check_tickets(gen, S, k, l))
        self.assertEqual(len(gen), 2)

        S = list(range(1, 11))
        k = 6
        l = 3
        gen = q1_27.gen_tickets(S, k, l)
        self.assertTrue(q1_27.check_tickets(gen, S, k, l))

        S = list(range(1, 16))
        k = 6
        l = 3
        self.assertTrue(
            q1_27.check_tickets(
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
            q1_27.check_tickets(
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


class TestP1_1(unittest.TestCase):
    def test(self):
        self.assertEqual(p1_1.solve(1, 10), "1 10 20")
        self.assertEqual(p1_1.solve(100, 200), "100 200 125")
        self.assertEqual(p1_1.solve(201, 210), "201 210 89")
        self.assertEqual(p1_1.solve(900, 1000), "900 1000 174")
        self.assertEqual(p1_1.solve(1000, 900), "1000 900 174")
        # Worst case input:
        self.assertEqual(p1_1.solve(1, 9999), "1 9999 262")


class TestP1_3(unittest.TestCase):
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
        self.assertEqual(p1_3.solve(p1_3.parse(inp)), ["John Doe"])

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
        self.assertEqual(p1_3.solve(p1_3.parse(inp)), ["John Doe", "", "a", "b"])


class TestL2_1(unittest.TestCase):
    def test(self):
        s = l2_1.Solution()

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


class TestL2_3(unittest.TestCase):
    def test(self):
        s = l2_3.Solution()
        self.assertEqual(
            sorted([sorted(l) for l in s.fourSum([1, 0, -1, 0, -2, 2], 0)]),
            sorted(sorted(l) for l in [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        )
        self.assertEqual(s.fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])


if __name__ == "__main__":
    unittest.main()
