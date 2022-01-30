from collections import Counter


def count_words(sentence: str) -> dict:
    c = Counter(sentence.split())
    return dict(c)
