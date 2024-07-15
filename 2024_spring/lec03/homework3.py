

def cancellation(list, stop_word):
    output = []
    for element in list:
        if element == stop_word:
            break
        output.append(element)
    return output


def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for element in input_list:
        if element == skip_word:
            continue
        output_list.append(element)
    return output_list


def my_average(input_list):
    total = sum(input_list)
    count = len(input_list)
    average = total / count
    return average

