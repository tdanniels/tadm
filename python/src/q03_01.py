# start snippet balanced-parens
def balanced_parens(x: str) -> bool:
    """
    Returns true if `x` consists only of balanced parentheses.
    Returns false otherwise.
    """
    left_parens = []
    for i, p in enumerate(x):
        if p == "(":
            left_parens.append(i)
        elif p == ")":
            try:
                left_parens.pop()
            except IndexError:
                print(f"Unbalanced ')' at position {i} of {x}.")
                return False
        else:
            raise ValueError(f"Invalid character {p} in {x}.")
    if left_parens:
        print(f"Unbalanced '(' at position {left_parens[0]} of {x}.")
        return False
    return True
    # end snippet balanced-parens
