def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    unique = {c for c in sentence.lower() if c.isalpha()}
    return alphabet.issubset(unique)
