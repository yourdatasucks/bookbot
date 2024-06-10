def main():
    book_location = "books/frankenstein.txt"
    contents = open_book(book_location)
    first_line = contents.partition("\n")[0]
    # print(f"First line is:\n{first_line}")
    wc = word_count(contents)
    cc = char_count(contents)
    print(f"This document contains {wc} words.")
    print(f"This document contains {cc}")
def open_book(path):
    with open(path)as f:
        return f.read()
def word_count(text):
    words = text.split()
    return len(words)
def char_count(text):
    chars_dict = {} # String(character) -> Integer(num_times_appeared)
    words = text.split()
    for word in words:
        for char in word:
            char = char.lower()
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict
if __name__ == '__main__':
    main()
