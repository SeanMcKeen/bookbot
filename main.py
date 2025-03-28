from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_list
import sys

def get_book_text(filePath):
    f_contents = ""
    with open(filePath) as f:
        f_contents = f.read()
    return f_contents

def print_report(bookpath, wc, s_char_c):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for dict in s_char_c:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = get_word_count(book_contents)
    character_count = get_character_count(book_contents)
    sorted_char_count = get_sorted_list(character_count)

    print_report(book_path, word_count, sorted_char_count)

    

main()