import string

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
    

def preprocess_text(text: str) -> str:
    """
    Preprocess a text string.

    converts the text to lowercase.
    removes all punctuation.
    keeps the words separated by single spaces.

    Args:
        text (str): The raw text.

    Returns:
      str: The lowercase text with punctuation removed and single spaces
      between words.
      
    """
    
    no_punct = ""
    for ch in text:
        if ch not in string.punctuation:
            no_punct += ch
    
    words = no_punct.split()
    return " ".join(words).lower()

test_texts = [
    'Hello, World!',
    '  Python is GREAT!!!  ',
    "It's 5 o'clock, isn't it?",
    ''
]

for raw in test_texts:
    print(f"{raw!r} -> {preprocess_text(raw)!r}")