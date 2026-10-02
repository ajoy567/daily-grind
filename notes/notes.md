# Daily notes

## Day 1

- Clicked: split() with no arguments removes extra spaces on its own, and " ".join(list) puts the words back together.
- Confused: I tried calling .join() on a list, but join belongs to the separator string.
- Remember: test empty and all-space inputs, because those are where functions break.
- ML twist: removed punctuation by looping over characters and keeping the ones not in string.punctuation. Models need clean text so "Hello," and "hello" count as the same word.

## Day 2

- Clicked: edge cases are inputs that pass the main rules but are still wrong. One if per case, each with its own reason.
- Confused: forgot how to find edge cases. Ask "what's the weirdest input that still passes?"
- Remember: check the simple rules first, then split.
