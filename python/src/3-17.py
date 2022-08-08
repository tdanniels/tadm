from collections import Counter

CHARFREQS = {
    "a": 0.08167,
    "b": 0.01492,
    "c": 0.02782,
    "d": 0.04253,
    "e": 0.12702,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.06966,
    "j": 0.00153,
    "k": 0.00772,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.05987,
    "s": 0.06327,
    "t": 0.09056,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.02360,
    "x": 0.00150,
    "y": 0.01974,
    "z": 0.00074,
}


def caesar(s: str, m: dict[str, str]) -> str:
    """
    Apply the Caesar cipher encoded by `m` to `s`. `m` should be a dict with 26
    entries, one for each lower-case letter of the English alphabet, that maps
    each character to another character.
    """
    return "".join(m[c.lower()] if c.isalpha() and c.isascii() else c for c in s)


def frequency_analysis(ctext: str) -> dict[str, str]:
    """
    Performs frequency analysis on the ciphertext `ctext` to derive a bijective
    mapping from `S` to `S`, where `S` is the lower-case characters of the
    English alphabet.

    Assumption: `c` is standard ASCII English text encoded with a Caesar
    cipher.
    """
    counts = Counter()
    for c in ctext:
        if c.isascii() and c.isalpha():
            counts[c] += 1
    scfreqs = reversed(sorted(CHARFREQS.items(), key=lambda x: x[1]))

    return {c[0]: v[0] for (c, v) in zip(counts.most_common(), scfreqs)}
