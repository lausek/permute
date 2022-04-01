from permute import Permute


def test_one_word():
    words = ["a"]
    permute = Permute(words)

    assert 1 == permute.amount()
    assert "a" in list(permute.create_generator())


def test_two_words():
    words = ["a", "b"]
    permute = Permute(words)

    assert 4 == permute.amount()
    result = list(permute.create_generator())
    assert "a" in result
    assert "b" in result
    assert "ab" in result
    assert "ba" in result


def test_three_words():
    words = ["a", "b", "c"]
    permute = Permute(words)

    assert 15 == permute.amount()
    result = list(permute.create_generator())
    assert "a" in result
    assert "b" in result
    assert "c" in result
    assert "ab" in result
    assert "ac" in result
    assert "ba" in result
    assert "bc" in result
    assert "ca" in result
    assert "cb" in result
    assert "abc" in result
    assert "acb" in result
    assert "bac" in result
    assert "bca" in result
    assert "cab" in result
    assert "cba" in result


def test_four_words():
    words = ["a", "b", "c", "d"]
    permute = Permute(words)

    assert 64 == permute.amount()
    result = list(permute.create_generator())
    assert 64 == len(result)
