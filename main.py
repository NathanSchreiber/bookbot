from stats import word_count, character_count

#returns opened file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#provides get_book_text with relative path to Frankenstein and prints result
def main():
    text = "./books/frankenstein.txt"
    return get_book_text(text)

#holds dictionary of letters
char_count = character_count(main());

print(f"Found {word_count(main())} total words")
print(char_count);