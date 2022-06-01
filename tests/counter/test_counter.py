from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word_py = "Python"
    word_js = "Javascript"

    assert count_ocurrences(path, word_py) == 1639
    assert count_ocurrences(path, word_js) == 122
