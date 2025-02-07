"""Utils Test Ex05."""
__author__ = "730311638"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Test only_evens when empty."""
    even_and_odds: list[int] = []
    assert only_evens(even_and_odds) == []


def test_only_evens_many() -> None:
    """Test only_evens when many items."""
    even_and_odds: list[int] = [2, 4, 6]
    assert only_evens(even_and_odds) == [2, 4, 6]


def test_only_evens_many_again() -> None:
    """Test only_evens with many items again."""
    even_and_odds: list[int] = [-3, -2, -1, 0, 3, 2, 12, 18]
    assert only_evens(even_and_odds) == [-2, 0, 2, 12, 18]


def test_concat_empty() -> None:
    """Test concat when empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_many() -> None:
    """Test concat with many items."""
    x: list[int] = [0, 1, 2]
    y: list[int] = [3, 4, 5]
    assert concat(x, y) == [0, 1, 2, 3, 4, 5]


def test_concat_many_again() -> None:
    """Test concat with many items again."""
    x: list[int] = [-2, -3, -40]
    y: list[int] = [100, 550, 730]
    assert concat(x, y) == [-2, -3, -40, 100, 550, 730]


def test_sub_empty() -> None:
    """Test sub when empty."""
    x: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(x, start, end) == []


def test_sub_many() -> None:
    """Test sub with many."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 2
    end: int = 5
    assert sub(x, start, end) == [3, 5]


def test_sub_many_again() -> None:
    """Test sub with many again."""
    x: list[int] = [10, 20, 30, 40, 50, 60, 70, 80]
    start: int = 1
    end: int = 10
    assert sub(x, start, end) == x[start]