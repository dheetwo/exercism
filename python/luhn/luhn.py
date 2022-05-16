class Luhn:
    card_string = ""

    def __init__(self, card_num):
        self.card_string = card_num

    def valid(self):
        card_list = []
        for character in self.card_string:
            if not character.isnumeric():
                if character != " ":
                    return False
            else:
                card_list.append(int(character))
        if len(card_list) < 2:
            return False
        for index, number in enumerate(card_list):
            if len(card_list) % 2 == 0:
                if index % 2 == 0:
                    if 0 <= number <= 4:
                        card_list[index] = 2 * number
                    else:
                        card_list[index] = 2 * number - 9
            else:
                if index % 2 != 0:
                    if 0 <= number <= 4:
                        card_list[index] = 2 * number
                    else:
                        card_list[index] = 2 * number - 9
        print(card_list)
        return sum(card_list) % 10 == 0

