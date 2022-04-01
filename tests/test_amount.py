from permute import Permute, permutation_amount


def test_amount_no_words():
    words = []
    permute = Permute(words)
    assert 0 == permute.amount()


def test_amount_one_word():
    words = ["a"]
    permute = Permute(words)
    assert 1 == permute.amount()


def test_amount_two_words():
    words = ["a", "b"]
    permute = Permute(words)
    assert 4 == permute.amount()


def test_amount_three_words():
    words = ["a", "b", "c"]
    permute = Permute(words)
    assert 15 == permute.amount()


def test_amount_uppercase():
    words = ["aa", "bb"]
    permute = Permute(words, with_uppercase=True)
    assert 64 == permute.amount()
    result = list(permute.create_generator())
    assert "aaAA" in result
    assert "aaaa" not in result
    assert "aaBB" in result
    assert "aabb" in result


def test_amount_lowercase():
    words = ["AA", "BB"]
    permute = Permute(words, with_lowercase=True)
    assert 64 == permute.amount()
    result = list(permute.create_generator())
    assert "aaAA" in result
    assert "aaaa" not in result
    assert "aaBB" in result
    assert "aabb" in result


def test_only_unique_words_added():
    words = ["b", "b"]
    permute = Permute(words)
    assert 1 == permute.amount()


def test_permutation_computation():
    assert 1 == permutation_amount(1)
    assert 4 == permutation_amount(2)
    assert 15 == permutation_amount(3)
    assert 64 == permutation_amount(4)

    assert 0 == permutation_amount(0)
    assert 0 == permutation_amount(-1)
