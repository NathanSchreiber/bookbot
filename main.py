#returns opened file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#provides get_book_text with relative path to Frankenstein and prints result
def main():
    text = "./books/frankenstein.txt"
    #print(get_book_text(text))
    return get_book_text(text)


#main()


def word_count(text):
    split_text = text.split()
    return len(split_text)

print(f"Found {word_count(main())} total words")