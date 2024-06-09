def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        first_line = file_contents.partition("\n")
        print(f"The first line of the file is:\n{first_line[0]}")


if __name__ == '__main__':
    main()
