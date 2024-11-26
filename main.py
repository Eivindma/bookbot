book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def wordcount():
    text = get_book_text(book_path)
    words = text.split()
    wordcount = 0
    for i in words:
        wordcount += 1
    print(wordcount)
    
def character_count():
    
    


main()

wordcount()



    
