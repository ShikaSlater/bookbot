def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    count = file_contents.split()
    word_count = len(count)
    return word_count