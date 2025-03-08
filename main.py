def main():
    import sys
    from stats import get_book_text
    from stats import get_num_words
    from stats import get_num_characters
    from stats import char_dict_sort

    if len(sys.argv) !=2:
        print(f"Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_count = get_num_words(text)
    char_count = get_num_characters(text)
    sort_char = char_dict_sort(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
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