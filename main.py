from stats import get_num_words
from stats import get_character_tally

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Get count of words
#def main():
#    num_words = len(get_num_words(get_book_text("books/frankenstein.txt")))
#    print(f"{num_words} words found in the document")

#get tally of characters
def main():
    character_tally = get_character_tally(get_book_text("books/frankenstein.txt"))
    print(character_tally)

main()