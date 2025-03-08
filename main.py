def main():
    from stats import get_book_text
    from stats import get_num_words
    from stats import get_num_characters
    from stats import char_dict_sort

    text = get_book_text(path_to_file = "books/frankenstein.txt")
    word_count = get_num_words(text)
    char_count = get_num_characters(text)
    sort_char = char_dict_sort(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_char:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()