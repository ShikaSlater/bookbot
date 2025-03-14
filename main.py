def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    test_print = get_book_text("books/frankenstein.txt")
    print (test_print)


if __name__ == "__main__":
    main()