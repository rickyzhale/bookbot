import sys

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        book_contents = f.read()
        return book_contents
    

def main():
    flurp = get_book_text()
    print (flurp)


def word_count():
    flurp = get_book_text()
    words = flurp.split()
    num_words = len(words)
    print (f"Found {num_words} total words")

def count_characters():
    char_count = {}
    flurp = get_book_text()
    lower = flurp.lower()
    for f in lower:
        if f in char_count:
            char_count[f] += 1
        else:
            char_count[f] = 1
    return char_count


def sort_on(char_count):
    return char_count["num"]

def get_sorted_char_list(char_count):
    letters = []
    for char in char_count:
        value = char_count[char]
        my_dict = {"char": (char), "num": (value)}
        letters.append(my_dict)
    letters.sort(reverse=True, key=sort_on)
    return letters

