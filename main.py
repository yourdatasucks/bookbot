def main():
    book_location = "books/frankenstein.txt"
    contents = open_book(book_location)
    first_line = contents.partition("\n")[0]
    # print(f"First line is:\n{first_line}")
    wc = word_count(contents)
    cc = char_count(contents)
    #print(f"This document contains {wc} words.")
    #print(f"This document contains {cc}")
    sorted_char_list = char_list_sort(cc)
    report(wc,sorted_char_list)
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
def char_list_sort(cc_dict):
    sorted_list = []
    for char in cc_dict:
        sorted_list.append({"char": char, "num_times": cc_dict[char]})
    sorted_list.sort(key=sort_on)
    return sorted_list
def sort_on(dictionary):
    return dictionary['num_times']
def report(wc, cc_sorted_list):
    # print the word count of the document
    # passing in an int as the word count so this is easy
    print(f"This document contains {wc} words.")

    # print the character and the number of times that character appeared in the document
    # passing in a list of dictionaries, example, "char": 'a', "num_times": 5
    for thing in cc_sorted_list:
        if thing['char'].isalpha() == False:
            continue
        print(f"The letter {thing['char']} appeared {thing['num_times']} number of times")
if __name__ == '__main__':
    main()
