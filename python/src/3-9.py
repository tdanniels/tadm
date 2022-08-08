from bst import BST


# start snippet concat-bsts
def concatenate(s1: BST, s2: BST) -> BST:
    """Assumption: all values in `s2` are greater than any in `s1`."""
    new_root = s1.find_max()
    if (parent := new_root.parent) is not None:
        parent.right = None

    new_root.left = s1
    new_root.right = s2
    return new_root
    # end snippet concat-bsts
