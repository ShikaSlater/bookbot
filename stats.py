def get_word_count(text_file):
    with open(text_file, 'r') as f:
        file_contents = f.read()
    count = file_contents.split()
    word_count = len(count)
    return word_count

def get_character_count(text_file):
    with open(text_file, 'r') as f:
        file_contents = f.read()
    char_counts = {}
    for char in file_contents:
            if char.isalpha():
                char = char.lower()
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts