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
    list_to_return = []
    for letter in letter_count:
        list_to_return.append({"char": letter, "num": letter_count[letter]})

    list_to_return.sort(reverse=True, key=sort_by)
    return list_to_return


def sort_by(items):
    return items["num"]
