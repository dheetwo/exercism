def abbreviate(words):
    words2 = words.replace("-", " ")
    words_list = words2.split(" ")
    acronym_list = []
    for item in words_list:
        if any(c.isalpha() for c in item):
            for i in item:
                if i.isalpha():
                    acronym_list.append(i.upper())
                    break
    return "".join(acronym_list)

print(abbreviate("Halley's Comet"))
print(abbreviate("Something - I made up from thin air"))
print(abbreviate("The Road _Not_ Taken"))

