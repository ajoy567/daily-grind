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

## Day 4

- Clicked: check for problems first, change the data last. In sell(), the checks (bad qty, missing item, not enough stock) come before the subtraction, and each `raise` stops the function.
- Bug I made: I put the checks after the sale, so a valid sale still raised an error. Order matters.
- Remember: edge case = the unusual situation. `if` detects it and `raise` reports it. `try/except` is for the code that calls the function.
- Weird inputs I tested: qty 0, negative qty, missing item, selling more than the stock, selling exactly the stock (item deleted), qty equal to the threshold in low_stock.
- Docstring trick: answer four questions. What does it do? What goes in? What comes out? What can go wrong?
