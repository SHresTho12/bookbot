import sys

from stats import book_words, get_char_count , dic_to_sorted_list

def get_book_text(file_path):
    book_content =""
    with open(file_path) as f:
        book_content = f.read()
    return book_content



def main():
    file_path = ""
    if len(sys.argv) <2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        
    
    book_content = get_book_text(file_path)
    num_words = book_words(book_content)
    char_count = get_char_count(book_content)
    char_count_list = dic_to_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in char_count_list:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["count"]}")
    print("============= END ===============")    
    
main()