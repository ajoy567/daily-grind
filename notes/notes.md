# Daily notes

## Day 1

- Clicked: split() with no arguments removes extra spaces on its own, and " ".join(list) puts the words back together.
- Confused: I tried calling .join() on a list, but join belongs to the separator string.
- Remember: test empty and all-space inputs, because those are where functions break.
- ML twist: removed punctuation by looping over characters and keeping the ones not in string.punctuation. Models need clean text so "Hello," and "hello" count as the same word.

## Day 2

- Clicked: an edge case is an input that passes the main rules but is still wrong. I add one `if` per case, each with its own reason.
- Confused: I forgot how to find edge cases. Trick: ask "what's the weirdest input that still passes?"
- Bug I made: in my second loop I wrote `for mail in ...` but called `is_valid_email(email)`. It ran without an error but gave 100% instead of 87.5%. Loop variable names must match what I use inside.
- ML twist: counted invalid emails and printed the percent. This is a basic data quality check before training a model.

## Day 3

- Clicked: split, guard, take, count. Check that the list isn't empty before using [0].
- Bug I made: put the empty check after split()[0], so it crashed before the check ran. Also tried to format a whole dict with :.2f, but formatting only works on one number at a time, so I looped over the dict.
- ML twist: percentages of each label show class imbalance. A model can look accurate just by always guessing the biggest class.
