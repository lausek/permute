from typing import Generator, List, Optional, Set


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


def create_permutation(words: Set[str]) -> Generator[str, None, None]:
    yield from words

    word_n = len(words)

    if word_n <= 1:
        return

    if word_n == 2:
        for word in words:
            for other_word in words - set([word]):
                yield word + other_word
        return

    for word in words:
        for combined_word in create_permutation(words - set([word])):
            yield word + combined_word


class Permute:
    def __init__(
        self, words: List[str], min_len: int = 0, max_len: Optional[int] = None
    ):
        self.words = set(words)
        self.min_len = min_len
        self.max_len = max_len

        if self.min_len < 0:
            raise Exception(
                f"invalid minimum length '{self.min_len}'. must be at least 0."
            )

        if self.max_len is not None and self.max_len < 1:
            raise Exception(
                f"invalid maximum length '{self.max_len}'. must be at least 1."
            )

    def create_generator(self) -> Generator[str, None, None]:
        for word in create_permutation(self.words):
            word_n = len(word)

            if word_n < self.min_len or (
                self.max_len is not None and self.max_len < word_n
            ):
                continue

            yield word

    def amount(self) -> int:
        return permutation_amount(len(self.words))
