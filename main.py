def main():
    book_location = "books/frankenstein.txt"
    contents = open_book(book_location)
    # first_line = contents.partition("\n")[0]
    # print(f"First line is:\n{first_line}")
    wc = word_count(contents)
    print(f"This document contains {wc} words.")
def open_book(path):
    with open(path)as f:
        return f.read()
def word_count(text):
    words = text.split()
    return len(words)
if __name__ == '__main__':
    main()
