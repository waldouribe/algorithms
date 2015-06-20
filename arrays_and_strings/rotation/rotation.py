# def rotation(a_string, another_string):
#     concat = a_string + a_string
#     return is_contained_in(a_string, another_string)

def rotation(a_string, another_string):
    if len(a_string) != len(another_string):
        return False

    length = len(a_string)
    a_string_index = 0
    another_string_index = 0
    number_of_matches = 0
    comparisons = 0

    while(another_string_index < length):
        if another_string[another_string_index] == a_string[a_string_index]:
            number_of_matches += 1
            another_string_index += 1
        else:
            number_of_matches = 0
            another_string_index = 0
        comparisons += 1
        a_string_index = (a_string_index+1)%length
        if comparisons >= 2*length:
            break

    return number_of_matches == length

def is_contained_in(container, content):
    return container.find(content) != -1
