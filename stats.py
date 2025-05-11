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