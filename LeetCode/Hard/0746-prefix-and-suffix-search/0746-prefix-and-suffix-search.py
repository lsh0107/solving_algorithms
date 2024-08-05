class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_suffix_map = {}

        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                prefix = word[:i]
                for j in range(length + 1):
                    suffix = word[j:]
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) in self.prefix_suffix_map:
            return self.prefix_suffix_map[(pref, suff)]
        return -1