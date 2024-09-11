def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    chars_sorted_list = num_chars_to_char_list(num_chars)

    print("--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for dict in chars_sorted_list:
        if not dict["char"].isalpha():
            continue
        print(f"The '{dict['char']}' character was found '{dict['count']}' times")
    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


def num_chars_to_char_list(num_chars):
    char_list = []
    for char in num_chars:
        char_list.append({"char": char, "count": num_chars[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


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