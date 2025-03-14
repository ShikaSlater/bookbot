from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    test_print = get_book_text("books/frankenstein.txt")
    wc = get_word_count("books/frankenstein.txt")
    print (f"{wc} words found in the document")
    print (test_print)


if __name__ == "__main__":
    main()