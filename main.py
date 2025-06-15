import sys
from stats import count_characters
from stats import get_sorted_char_list
from stats import word_count
from stats import sort_on

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count()
    print("--------- Character Count -------")
    char_count = count_characters()
    result = get_sorted_char_list(char_count)
    for char in result:
        char_value = char["char"]
        char_num = char["num"]
        if char_value.isalpha() == True:
            print(f"{char_value}: {char_num}")
    print("============= END ===============")

main()