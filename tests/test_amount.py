from permute import Permute, permutation_amount


def test_amount_no_words():
    words = set([])
    permute = Permute(words)
    assert 0 == permute.amount()


def test_amount_one_word():
    words = set(["a"])
    permute = Permute(words)
    assert 1 == permute.amount()


def test_amount_two_words():
    words = set(["a", "b"])
    permute = Permute(words)
    assert 4 == permute.amount()


def test_amount_three_words():
    words = set(["a", "b", "c"])
    permute = Permute(words)
    assert 15 == permute.amount()


def test_permutation_computation():
    assert 1 == permutation_amount(1)
    assert 4 == permutation_amount(2)
    assert 15 == permutation_amount(3)
    assert 64 == permutation_amount(4)

    assert 0 == permutation_amount(0)
    assert 0 == permutation_amount(-1)
