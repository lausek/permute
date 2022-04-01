from typing import Set


def permutation_amount(alphabet_n: int) -> int:
    """
    This computes the possible permutations for a set of `alphabet_n` words:
    permutation_amount(1) = 1
    permutation_amount(n) = n + n*permutation_amount(n - 1) = n * (1 + permutation_amount(n - 1))
    """
    if alphabet_n <= 0:
        return 0
    x = 0
    for i in range(1, alphabet_n + 1):
        x += 1
        x *= i
    return x


class Permute:
    def __init__(self, words: Set[str]):
        self.words = words

    def amount(self) -> int:
        return permutation_amount(len(self.words))
