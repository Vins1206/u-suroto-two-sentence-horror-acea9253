#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences (under 400
characters) to /output/entry.txt. Pure standard library, no
network, no randomness: every run writes the same bytes.

The story is built for the published judge brief: the first
sentence sets a calm, clinical scene, and the second sentence
turns it — the harmless "shadow" is alive — so the first
sentence reads worse the second time. The horror is implied,
never explained, and every word earns its place.
"""

import os

STORY = (
    "The dentist showed me my X-ray and pointed to a small shadow "
    "inside my jaw, saying it was nothing to worry about. "
    "When I got home, I opened my mouth in the mirror and the "
    "shadow blinked."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The harness mounts the kit at /kit; read it when present so the
    # program honours the kit contract, but the story itself is fixed.
    try:
        with open("/kit/kit.txt", "r", encoding="utf-8") as handle:
            handle.read()
    except OSError:
        pass
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
