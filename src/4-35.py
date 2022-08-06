from typing import Optional, Tuple

# start snippet saddleback
def saddleback(mat, sought):
    nrows = len(mat)
    i = nrows - 1
    j = 0
    while i >= 0 and j < len(mat[0]):
        if mat[i][j] == sought:
            return (i, j)
        elif mat[i][j] > sought:
            i -= 1
        else:
            j +=1
    return None
    # end snippet saddleback

# start snippet binary-search-2d
def binary_search_2d(
    mat: list[list[int]],
    sought: int,
    window_v: Tuple[int, int],
    window_h: Tuple[int, int],
) -> Optional[Tuple[int, int]]:
    if len(mat) == 0 or len(mat[0]) == 0:
        return None

    if window_h[0] > window_h[1] or window_v[0] > window_v[1]:
        return None

    mid_v = (window_v[0] + window_v[1]) // 2
    mid_h = (window_h[0] + window_h[1]) // 2

    if mat[mid_v][mid_h] == sought:
        return (mid_v, mid_h)

    if mat[mid_v][mid_h] > sought:
        # Check upper left, upper right, bottom left
        return (
            binary_search_2d(
                mat, sought, (window_v[0], mid_v - 1), (window_h[0], mid_h - 1)
            )
            or binary_search_2d(
                mat, sought, (window_v[0], mid_v - 1), (mid_h, window_h[1])
            )
            or binary_search_2d(
                mat, sought, (mid_v, window_v[1]), (window_h[0], mid_h - 1)
            )
        )
    else:
        # Check upper right, bottom left, bottom right
        return (
            binary_search_2d(
                mat, sought, (window_v[0], mid_v), (mid_h + 1, window_h[1])
            )
            or binary_search_2d(
                mat, sought, (mid_v + 1, window_v[1]), (window_h[0], mid_h)
            )
            or binary_search_2d(
                mat, sought, (mid_v + 1, window_v[1]), (mid_h + 1, window_h[1])
            )
        )
    # end snippet binary-search-2d
