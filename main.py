def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this document")
    counts = letter_count(text)
    sorted_counts = sort_letters(counts)
    for item in sorted_counts:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End report ---")

def letter_count(text):
    lower = text.lower()
    letter_counts = {}
    for x in lower:
        if x in letter_counts:
            letter_counts[x] +=1
        elif x.isalpha():
            letter_counts[x] = 1
    return letter_counts 

def sort_letters(letter_counts):
    letter_list = [{'letter': letter, "count": count} for letter, count in letter_counts.items()]

    def sort_on(dict_item):
        return dict_item['count']

    letter_list.sort(reverse=True, key=sort_on)

    return letter_list

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()