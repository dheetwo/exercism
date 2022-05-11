def is_isogram(string):
    letters_used = set()
    for character in string:
        if character.lower() in letters_used:
            return False
        elif character.isalpha():
            letters_used.add(character.lower())
    return True

