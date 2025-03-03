import sys
from stats import get_book_word_count, count_characters, sort_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    #path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("usage: pyron3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    word_count = get_book_word_count(path)
    print(f"Found {word_count} total words")
    
    # Get the text and count characters
    text = get_book_text(path)
    char_count = count_characters(text)
    
    # Get sorted list of character counts
    sorted_chars = sort_char_count(char_count)
    
    # Print character count section
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print report footer
    print("============= END ===============")

# Call main function
main()