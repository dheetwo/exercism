def find_anagrams(word, candidates):
    # for loop running through each word in candidate list
    anagram_list = []
    for item in candidates:
        # nested loop running through each character in a candidate
        if candidate_is_anagram(word, item):
            anagram_list.append(item)
    return anagram_list


def candidate_is_anagram(word, candidate):
    if word.casefold() == candidate.casefold() or len(word) != len(candidate):
        return False
    else:
        for character in candidate:
            if character.lower() in word:
                word = word.replace(character.lower(), "", 1)
            elif character.upper() in word:
                word = word.replace(character.upper(), "", 1)
            else:
                return False
    return True
