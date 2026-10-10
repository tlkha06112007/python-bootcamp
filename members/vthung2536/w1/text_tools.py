
from collections import Counter
import string


def word_count(text: str) -> dict[str, int]:
    """Count words case-insensitively, ignoring punctuation."""
    punctuation = ".,!?;:"
    translation_table = str.maketrans(
        {char: " " for char in punctuation}
    )

    words = text.lower().translate(translation_table).split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted by count then alphabetically."""
    if k <= 0:
        return []

    counts = word_count(text)
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]
