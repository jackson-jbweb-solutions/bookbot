def count_letters(book_contents):
    words = book_contents.split()
    letter_count = {}
    for word in words:
        for letter in word:
            char = letter.lower()
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1

    return letter_count, len(words)


def sorted_list(letter_count):
    print(letter_count)
