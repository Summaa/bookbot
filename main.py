def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = get_word_count(text)
    char_dict = get_character_dict(text)
    print_report(book_path, word_count, char_dict)
    

def get_book_contents(path):
    with open(path) as book:
        return book.read()

def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def get_character_dict(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def print_report(book, word_count, char_dict):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print("")

    char_list = []
    for char in char_dict:
        char_count = char_dict[char]
        if char.isalpha():
            char_list.append([char_count, char])
    char_list.sort(reverse=True)

    for char in char_list:
        print(f"The {char[1]} character was found {char[0]} times")
    print("--- End report ---")


main()