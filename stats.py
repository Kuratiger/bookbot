def get_num_words(book_text):
    word_count = book_text.split()
    return word_count

def get_character_tally(book_text):
    character_tally = {}
    lowered_book_text = book_text.lower()
    for char in lowered_book_text:
        character_tally[char] = 0
    for char in lowered_book_text:
        character_tally[char] += 1
    return character_tally

def sort_on(dict):
    return dict["num"]

def get_ordered_character_tally(character_tally):
    # init list
    ordered_character_tally = []
    #ccreate list of dictionaries
    for char in character_tally:
        if char.isalpha() == True:
            ordered_character_tally.append({"char": char, "num": character_tally[char]})
    #order list of dictionaries        
    ordered_character_tally.sort(reverse=True, key=sort_on) # I do not understand how tf sort_on actually works here but fuckit.

    return ordered_character_tally
