def comma_code(word_list):
    # handle empty list or single element list
    if len(word_list) == 0:
        return word_list[0]
    elif len(word_list) == 1:
        return ""

    word_end = " and " + word_list[-1]
    word_start = ", ".join(word_list[:-1])
    return word_start + word_end


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_code(spam))
