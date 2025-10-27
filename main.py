from stats import get_num_words, get_letter_count, sort_char
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    get_num_words(book_text)
    letters = get_letter_count(book_text)
    sorted_letters = sort_char(letters)
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
main()
