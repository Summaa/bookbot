def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = get_word_count(text)
    print(word_count)

def get_book_contents(path):
    with open(path) as book:
        return book.read()

def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

main()