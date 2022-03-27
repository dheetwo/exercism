def acceptable_syntax(str, lst):
    return str in lst or str.isnumeric()

def answer(question):
    question_list = question.split(" ")
    question_list[-1] = question_list[-1][:-1]
    numbers_list = []
    operations_list = []
    valid_queries = ["What"]
    valid_operations = ["plus", "minus", "multiplied", "divided"]
    if not question_list[0] in valid_queries:
        raise ValueError("unknown operation")
    del question_list[:2]
    if len(question_list) == 0:
        raise ValueError("syntax error")
    elif len(question_list) == 1:
        return int(question_list[0])
    while len(question_list) > 0:
        try:
            numbers_list.append(int(question_list[0]))
        except ValueError:
            print("NaN")
            raise ValueError("syntax error")
        if len(question_list) == 0:
            raise ValueError("syntax error")
        question_list.pop(0)
        if len(question_list) == 0:
            break
        if not acceptable_syntax(question_list[0], valid_operations):
            raise ValueError("unknown operation")
        if question_list[0] == "plus":
            operations_list.append("plus")
            del question_list[:1]
        elif question_list[0] == "minus":
            operations_list.append("minus")
            del question_list[:1]
        elif question_list[0] == "multiplied" and question_list[1] == "by":
            operations_list.append("multiplied by")
            del question_list[:2]
        elif question_list[0] == "divided" and question_list[1] == "by":
            operations_list.append("divided by")
            del question_list[:2]
        else:
            raise ValueError("syntax error")
    answer = numbers_list[0]
    numbers_list.pop(0)
    while len(operations_list) > 0:
        if len(numbers_list) == 0:
            raise ValueError("syntax error")
        if operations_list[0] == "plus":
            answer += numbers_list[0]
        elif operations_list[0] == "minus":
            answer -= numbers_list[0]
        elif operations_list[0] == "multiplied by":
            answer *= numbers_list[0]
        elif operations_list[0] == "divided by":
            answer = int(answer / numbers_list[0])
        numbers_list.pop(0)
        operations_list.pop(0)
    return answer