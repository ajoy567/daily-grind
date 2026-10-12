import re

class Inventory:
    """Item -> quantity stock tracker."""

    def __init__(self, stock: dict[str, int] | None = None) -> None:
        """
        Create an inventory, optionally seeded with existing stock.

        Args:
            stock (dict[str, int] | None): Initial item -> quantity mapping.
                Copied, so the caller's dict is not mutated. Defaults to empty.
        """
        self.stock: dict[str, int] = dict(stock) if stock else {}


    def restock(self, item: str, qty: int) -> None:
        """
        Add stock for an item, creating the item if it is new.

        Args:
            item (str): Name of the item to restock.
            qty (int): Number of units to add. Must be above 0.

        Raises:
            ValueError: If qty is 0 or negative.
        """
        if qty <= 0:
            raise ValueError("Quantity to restock must be a positive integer.")
        self.stock[item] = self.stock.get(item, 0) + qty

    def sell(self, item: str, qty: int) -> None:
        """
        Remove stock for an item. The item is deleted if its stock reaches 0.

        Args:
            item (str): Name of the item to sell.
            qty (int): Number of units to sell. Must be above 0.

        Raises:
            ValueError: If qty is 0 or negative, if the item is not in the
                inventory, or if there is not enough stock.
        """
        if qty <= 0:
            raise ValueError("Quantity to sell must be a positive integer.")
        if item not in self.stock:
            raise ValueError(f"{item!r} is not in inventory.")

        available = self.stock[item]
        if available < qty:
            raise ValueError(
                f"Not enough {item!r} in inventory: "
                f"requested {qty}, available {available}."
            )

        self.stock[item] -= qty
        if self.stock[item] == 0:
            del self.stock[item]


    def low_stock(self, threshold: int) -> list[str]:
        """
        Find items whose quantity is below a threshold.

        Args:
            threshold (int): Items with a quantity strictly below this are
                included.

        Returns:
            list[str]: Names of the low-stock items. Empty if there are none.
        """
        return [item for item, qty in self.stock.items() if qty < threshold]

    def quantity_of(self, item: str) -> int:
        """
        Get the current quantity of an item.

        Args:
            item (str): Name of the item to look up.

        Returns:
            int: The quantity in stock, or 0 if the item is not in the
                inventory.
        """
        return self.stock.get(item, 0)


    def __contains__(self, item: str) -> bool:

        return item in self.stock
    

    def __getitem__(self, item: str) -> int:
        
        return self.stock[item]


    def __len__(self) -> int:
 
        return len(self.stock)


    def __repr__(self) -> str:

        return f"Inventory({self.stock!r})"

class Vocabulary:
    """Maps unique words to stable integer ids in first-seen order.

    A reserved ``<unk>`` id is always index 0 so unseen words can be encoded
    without silently disappearing.
    """

    UNK = "<unk>"
    _TOKEN_RE = re.compile(r"[a-zA-Z0-9']+")

    def __init__(self, sentences: str | list[str] | None = None) -> None:
        """
        Create a vocabulary, optionally seeded from one or more sentences.

        Args:
            sentences (str | list[str] | None): Text to build from. A single
                string is treated as one sentence. Defaults to an empty vocab
                containing only the ``<unk>`` token.
        """
        self._word_to_id: dict[str, int] = {self.UNK: 0}
        self._id_to_word: dict[int, str] = {0: self.UNK}
        if sentences is not None:
            self.add(sentences)


    @classmethod
    def _tokenize(cls, text: str) -> list[str]:
        """
        Split text into lowercase word tokens.

        Args:
            text (str): Raw text to tokenize.

        Returns:
            list[str]: Tokens, punctuation stripped, apostrophes kept.
        """
        return cls._TOKEN_RE.findall(text.lower())

    def add(self, sentences: str | list[str]) -> None:
        """
        Add one sentence or a list of sentences to the vocabulary.

        New words are assigned the next available integer id in first-seen
        order. Words already in the vocab are left alone.

        Args:
            sentences (str | list[str]): Text to add.
        """
        if isinstance(sentences, str):
            sentences = [sentences]
        for sentence in sentences:
            for token in self._tokenize(sentence):
                if token not in self._word_to_id:
                    new_id = len(self._word_to_id)
                    self._word_to_id[token] = new_id
                    self._id_to_word[new_id] = token


    def encode(self, sentence: str, unk: bool = True) -> list[int]:
        """
        Encode a sentence as a list of vocabulary ids.

        Args:
            sentence (str): Text to encode.
            unk (bool): If True, unknown words map to the ``<unk>`` id. If
                False, unknown words raise instead. Defaults to True.

        Returns:
            list[int]: One id per token, in order.

        Raises:
            KeyError: If ``unk`` is False and a token is not in the vocab.
        """
        out: list[int] = []
        for token in self._tokenize(sentence):
            if token in self._word_to_id:
                out.append(self._word_to_id[token])
            elif unk:
                out.append(self._word_to_id[self.UNK])
            else:
                raise KeyError(f"Unknown token {token!r}")
        return out

    def decode(self, ids: list[int]) -> list[str]:
        """
        Turn a list of vocabulary ids back into words.

        Args:
            ids (list[int]): Ids produced by ``encode``.

        Returns:
            list[str]: One word per id, in order.

        Raises:
            KeyError: If an id is not in the vocabulary.
        """
        return [self._id_to_word[i] for i in ids]


    def __len__(self) -> int:
        """
        Size of the vocabulary, including ``<unk>``.

        Returns:
            int: Number of distinct tokens.
        """
        return len(self._word_to_id)

    def __contains__(self, word: str) -> bool:
        """
        Check whether a word is in the vocabulary.

        Args:
            word (str): Word to check.

        Returns:
            bool: True if the word is in the vocab.
        """
        return word in self._word_to_id

    def __getitem__(self, word: str) -> int:
        """
        Look up the id of a word.

        Args:
            word (str): Word to look up.

        Returns:
            int: The integer id assigned to the word.

        Raises:
            KeyError: If the word is not in the vocabulary.
        """
        return self._word_to_id[word]

    def __iter__(self):
        """
        Iterate over the vocabulary's words.

        Returns:
            Iterator[str]: Word iterator in insertion order.
        """
        return iter(self._word_to_id)

    def __repr__(self) -> str:
        """
        Readable representation of the vocabulary.

        Returns:
            str: A string like ``Vocabulary(size=6, unk_id=0)``.
        """
        return f"Vocabulary(size={len(self)}, unk_id={self._word_to_id[self.UNK]})"
    


inv = Inventory({"pen": 50, "notebook": 20, "stapler": 3})

inv.restock("pen", 10)
inv.restock("eraser", 5)
inv.sell("notebook", 5)
inv.sell("stapler", 3)

print(inv)                          # Inventory({'pen': 60, 'notebook': 15, 'eraser': 5})
print(inv.low_stock(10))            # ['eraser']
print(inv.quantity_of("stapler"))   # 0

try:
    inv.sell("pen", 999)
except ValueError as e:
    print(e)
# Not enough 'pen' in inventory: requested 999, available 60

vocab = Vocabulary("Hello, world! Hello, Python. Python is great.")
print(vocab)                        # Vocabulary(size=6, unk_id=0)
print(vocab.encode("Hello Python")) # [1, 3]
print(vocab.encode("Hello Ziggy"))  # [1, 0]
print(vocab.decode([1, 0, 3]))      # ['hello', '<unk>', 'python']