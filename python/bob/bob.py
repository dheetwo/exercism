def response(hey_bob):
    message = hey_bob.replace("\t", " ")
    message = hey_bob.replace("\n", " ")
    message = hey_bob.replace("\r", " ")
    message = message.strip()
    message_list = message.split(" ")
    message_list = [value for value in message_list if value != ""]
    question = []
    if len(message_list) > 0:
        question = message_list[-1][-1] == "?"
    elif len(question) == 0:
        return "Fine. Be that way!"
    yell = [value for value in message_list if not value.islower()]
    letters = [value for value in message if value.isalpha()]
    yelling = tuple(i for i in message_list) == tuple(j for j in yell) and len(letters) > 0
    if yelling and question:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."