def get_book_word_count(path):
    with open(path) as f:
        text = f.read()
        words = text.split()
        return len(words)

def count_characters(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1  # Fixed line: chars[char] = 1, not char[char] = 1
    return chars

def sort_char_count(char_dict):
    # Create a list of dictionaries with char and count
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Sort from greatest to least by count
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list