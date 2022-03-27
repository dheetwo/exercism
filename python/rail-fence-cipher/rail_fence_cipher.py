import math

def encode(message, rails):
    encoded_message = [""] * rails
    rail_number = 0
    direction = 1
    for character in message:
        encoded_message[rail_number] += character
        rail_number += direction
        if rail_number == rails - 1 or rail_number == 0:
            direction *= -1
    return "".join(encoded_message)


def decode(encoded_message, rails):
    period_length = 2 * (rails - 1)
    position_list = []
    message_rows = []
    horizontal_position = 0
    vertical_position = 0
    for index, letter in enumerate(encoded_message):
        if index * period_length <= len(encoded_message):
            position_list.append(index * period_length)
        horizontal_position += 1
    for item in position_list:
        print(encoded_message[item])



decode("WECRLTEERDSOEEFEAOCAIVDEN", 3)
# decode("EIEXMSMESAORIWSCE", 5)
# decode("133714114238148966225439541018335470986172518171757571896261", 6)