def clean_name(name: str) -> str:
    """
    Clean a person's name.

    Removes leading and trailing whitespace, collapses repeated spaces
    between words into one, and converts the result to title case.

    Args:
        name (str): The raw name, e.g. '  aRiya   SEN '.

    Returns:
        str: The cleaned name, e.g. 'Ariya Sen'. Returns '' if the
        input is empty or only spaces.
    """
    words = name.split()
    return " ".join(words).title()


test_names = [
    "  aRiya   SEN ",
    "rahul",
    "   MARY    ANN   DSOUZA",
    "",
    "    ",
]

for raw in test_names:
    print(f"{raw!r} -> {clean_name(raw)!r}")