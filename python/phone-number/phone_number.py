class PhoneNumber:
    number = ""
    area_code = ""
    exchange_code = ""

    def __init__(self, number):
        self.number = number
        self.clean()
        self.area_code = self.number[0:3]
        print(self.area_code)
        self.exchange_code = self.number[3:6]
        print(self.exchange_code)
        self.validity_check()

    def clean(self):
        number_clean = ""
        for item in self.number:
            if item.isalpha() and len(number_clean) > 0:
                raise ValueError("letters not permitted")
            elif not self.valid_punctuation(item) and len(number_clean) > 0:
                raise ValueError("punctuations not permitted")
            elif item.isnumeric():
                number_clean = number_clean + item
        if len(number_clean) < 10:
            print(number_clean)
            raise ValueError("incorrect number of digits")
        if len(number_clean) > 11:
            raise ValueError("more than 11 digits")
        elif len(number_clean) == 11:
            if not(number_clean[0] == "1"):
                raise ValueError("11 digits must start with 1")
            number_clean = number_clean[1:len(number_clean)]
        self.number = number_clean
        print(self.number)

    def validity_check(self):
        print(self.area_code[0] == "0")
        if self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

    def pretty(self):
        return "(" + self.area_code + ")" + "-" + self.exchange_code + "-" + self.number[6:10]

    def valid_punctuation(self, character):
        allowed_characters = ["(", ")", ".", " ", "-"]
        return character.isnumeric() or character in allowed_characters

