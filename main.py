import sys

from stats import count_letters, sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    letter_list, word_count = count_letters(book_contents)
    letter_list_sorted = sorted_list(letter_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ------- ")

    for letter in letter_list_sorted:
        if not letter["char"].isalpha():
            continue
        print(f"{letter['char']}: {letter['num']}")

    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
