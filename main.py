import os
from stats import get_word_count
from stats import get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "~/bookbot-1/books/frankenstein.txt"
    expanded_path = os.path.expanduser(path)
    test_print = get_book_text(expanded_path)
    wc = get_word_count(expanded_path)
    cc = get_character_count(expanded_path)
    print (test_print)
    print (f"{wc} words found in the document")
    print (cc)
    


if __name__ == "__main__":
    main()