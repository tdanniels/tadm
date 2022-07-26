from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class BinTree:
    left: Optional[BinTree]
    right: Optional[BinTree]
    parent: Optional[BinTree]
    value: int

    # start snippet concat-binary-trees
    def concatenate(self, s2: BinTree) -> BinTree:
        """Assumption: all values in `s2` are greater than any in `self`."""
        new_root = self.find_max()
        if (parent := new_root.parent) is not None:
            parent.right = None

        new_root.left = self
        new_root.right = s2
        return new_root
        # end snippet concat-binary-trees

    def find_max(self) -> BinTree:
        if self.right is None:
            return self
        return self.right.find_max()
