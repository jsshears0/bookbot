def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_characters(text):
    num_characters = {}
    for i in text.lower():
        if i in num_characters:
            num_characters[i] += 1
        else:
            num_characters[i] = 1
    return num_characters

def char_dict_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list