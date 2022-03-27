def clean_word(word):
    clean = ""
    for index, character in enumerate(word):
        # print(index, character, len(word) - 1)
        if character == "'":
            if not(index == 0 or index == len(word) - 1):
                clean = clean + character
        elif character.isalpha():
            clean = clean + character.lower()
        elif character.isnumeric():
            clean = clean + character
    return clean.strip("'")


def count_words(sentence):
    sentence_clean_whitespace = ""
    index = 0
    for item in sentence:
        # print(item, item.isspace(), item == ",")
        if item.isspace() or item == "_":
            if len(sentence_clean_whitespace) > 0 and sentence_clean_whitespace[-1] == " ":
                continue
            else:
                sentence_clean_whitespace = sentence_clean_whitespace + " "
        elif item == ",":
            sentence_clean_whitespace = sentence_clean_whitespace + ", "
        else:
            sentence_clean_whitespace = sentence_clean_whitespace + item
        print(sentence_clean_whitespace)
        index += 1
    sentence_list = sentence_clean_whitespace.split(" ")
    sentence_list = [x for x in sentence_list if x]
    # print(sentence_list)
    cleaned_sentence_list = []
    for word in sentence_list:
        cleaned_sentence_list.append(clean_word(word))
    cleaned_sentence_list = [x for x in cleaned_sentence_list if x]
    print(cleaned_sentence_list)
    word_count = dict()
    for item in cleaned_sentence_list:
        if word_count.__contains__(item):
            word_count[item] += 1
        else:
            word_count[item] = 1
    return word_count


