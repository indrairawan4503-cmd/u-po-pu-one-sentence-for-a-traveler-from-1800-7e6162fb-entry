"""One sentence for a traveler from 1800: the internet as a post office
that never sleeps. Writes the sentence to /output/entry.txt first, then
to entry.txt next to this file (best effort; the grader sandbox may mount
the repo read-only)."""

import os

SENTENCE = (
    "Picture a post office that never sleeps, where a letter from any town "
    "on earth reaches you the instant it is written, and the answer is "
    "already in your hand before the ink on your quill is dry."
)


def main():
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 chars"
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    assert SENTENCE == SENTENCE.strip(), "no leading/trailing whitespace"
    assert "\n" not in SENTENCE, "must be a single line"
    assert "  " not in SENTENCE, "no double spaces"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "must be exactly one sentence with a single terminal period"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(SENTENCE)
    except OSError:
        pass
    print(f"{len(SENTENCE)} chars")
    print(SENTENCE)


if __name__ == "__main__":
    main()
