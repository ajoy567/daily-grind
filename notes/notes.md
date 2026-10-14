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

## Learning Notes

### 2026-10-12 — Inventory + Vocabulary

**Built:** stock tracker (`restock`, `sell`, `low_stock`) + vocab builder
(word -> int id, with `<unk>` at 0).

**Decided:**

- Sell to 0 deletes the key — keeps `low_stock` clean.
- `low_stock` uses `<` not `<=`.
- Regex `[a-zA-Z0-9']+` for tokenizing, keeps "don't" intact.
- Class > free functions once state + behavior belong together.

**Bug:** my first vocab counted frequencies, not ids. Also had
`split()` inside a per-character loop and a dead `vocab = " ".join`.

**Lesson:** silently dropping unknown words is the worst default.
Reserve `<unk>` or raise — don't hide tokenizer drift.

**Next:** test empty/punctuation-only input. Try incremental `add()`.

## Day 5 — Price calculator

**Theme:** defaults, validation on inputs, and `*args` unpacking.

## What I built

- `final_price(price, discount_pct=0, tax_pct=18)` — discount first, then
  tax on the reduced amount. Rounds to 2 decimals.
- `cart_total(*items)` — sums any number of `(price, qty)` pairs. No tax,
  no discount.

## Decisions I made (and why)

- **Order of operations:** discount → tax. Tax is charged on what the
  customer actually pays, not the sticker price. Documented in the docstring.
- **Fail loud, fail early:** invalid inputs raise `ValueError` at the call
  site. Returning `None` or a sentinel would force every caller to remember
  to check.
- **`cart_total` doesn't apply tax.** The spec doesn't ask for it, and
  keeping it as a pure sum keeps the function reusable.
- **Empty cart returns `0.0`.** Falls out of starting `total = 0` — the
  empty case isn't special.

## Mistakes I made

1. **Validated the result, not the input.** First version checked
   `discounted_price > 100` instead of `discount_pct > 100`. This both
   rejected valid discounts (e.g. 20% off a ₹1000 item) and let through
   invalid ones. Lesson: **check the input at the boundary, not the
   output.**
2. **Shadowed the function name.** Assigned `final_price = ...` inside
   `final_price()`. Works, but breaks if you ever call the function
   recursively or add code below. Renamed the local to `total`.
3. **Invented an input shape.** Wrote `cart_total` assuming items were
   objects with `.price` / `.quantity`, but the spec said plain tuples.
   Lesson: **read the spec literally the first time.**
4. **Docstring drifted from code.** Kept the old "objects with attributes"
   description after switching to tuple unpacking. Docstrings are contracts
   — they need to change with the code.

## Things I want to remember

- `*items` collects positional args into a **tuple of tuples**.
- `for price, qty in items:` — unpack in the loop header. Cleaner than
  `item[0]` / `item[1]`.
- `round(2.675, 2)` → `2.67`, not `2.68` (banker's rounding + float
  imprecision). Real money code uses `Decimal`.
- Docstring `Raises:` section must be updated whenever I add a new check.
