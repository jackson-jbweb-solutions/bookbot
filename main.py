from reports import report
from stats import count_letters, sorted_list


def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    # word_count = count_words(book_contents)
    letter_list, word_count = count_letters(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ------- ")

    print(sorted_list(letter_list))


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
