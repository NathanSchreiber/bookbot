from stats import word_count

#returns opened file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#provides get_book_text with relative path to Frankenstein and prints result
def main():
    text = "./books/frankenstein.txt"
    return get_book_text(text)

print(f"Found {word_count(main())} total words")