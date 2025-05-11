from stats import get_num_words
from stats import get_character_tally
from stats import get_ordered_character_tally
from sys import argv

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    #check if correct number of inputs
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    #get number of words and ordered tally
    num_words = len(get_num_words(get_book_text(argv[1])))
    ordered_character_tally = get_ordered_character_tally(get_character_tally(get_book_text(argv[1])))

    #print header
    print(f"""============ BOOKBOT ============
Analyzing book found at {argv[1]}...""")
    #print word count
    print(f"""----------- Word Count ----------
Found {num_words} total words""")
    #print ordered list
    print("--------- Character Count -------")
    for dictionary in ordered_character_tally:
        print(f"{dictionary["char"]}: {dictionary["num"]}")
    #print end
    print("============= END ===============")


main()