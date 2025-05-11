from stats import get_num_words
from stats import get_character_tally
from stats import get_ordered_character_tally

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Get count of words
#def main():
#    num_words = len(get_num_words(get_book_text("books/frankenstein.txt")))
#    print(f"{num_words} words found in the document")

#get tally of characters
#def main():
#    character_tally = get_character_tally(get_book_text("books/frankenstein.txt"))
#    print(character_tally)

#get ordered tally of characters
#def main():
#    ordered_character_tally = get_ordered_character_tally(get_character_tally(get_book_text("books/frankenstein.txt")))
#    print(ordered_character_tally)

def main():
    #get number of words and ordered tally
    num_words = len(get_num_words(get_book_text("books/frankenstein.txt")))
    ordered_character_tally = get_ordered_character_tally(get_character_tally(get_book_text("books/frankenstein.txt")))

    #print header
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...""")
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