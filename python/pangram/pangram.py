def is_pangram(sentence):
    letters_used = set()
    for character in sentence:
        if character.isalpha():
            letters_used.add(character.lower())
    return len(letters_used) == 26
