from src.counter import count_ocurrences


def test_counter():
    python_ocurrences = count_ocurrences("src/jobs.csv", "Python")
    javascript_ocurrences = count_ocurrences("src/jobs.csv", "JavaScript")

    assert python_ocurrences == 1639
    assert javascript_ocurrences == 122
