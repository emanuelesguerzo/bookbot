from stats import count_words, count_chars, sorted_list, sort_on
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    text = get_book_text(path)
    print(f"Found {count_words(text)} total words")
    chars_num = count_chars(text)
    sorted_chars = sorted_list(chars_num)
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()