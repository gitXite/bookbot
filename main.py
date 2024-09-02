def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(num_chars)


def get_num_chars(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()