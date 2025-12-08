import sys
from stats import report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_text = get_book_text(sys.argv[1])
        final_report = report(book_text)
        return final_report

print(main())
# get_num_words(book_text)
# print(get_character_count(book_text))