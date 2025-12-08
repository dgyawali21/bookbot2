def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    # print(word_list)
    # print(f"Found {num_words} total words")
    return num_words

def get_character_count(text):
    character_count = {}
    for line in text:
        for char in line:
            lower = char.lower()
            character_count[lower] = character_count.get(lower, 0) + 1
    return character_count

def report(text):
    characters = get_character_count(text)
    sorted_characters = sorted(characters.keys())
    total_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for key in sorted_characters:
        if not key.isalpha():
        # Skip keys that are not strings or do not consist only of letters
            continue
        value = characters[key]
        print(f"{key}: {value}")

    
