
def book_words(book_content):
    words = book_content.split()
    return len(words)

def get_char_count(book_content):
    char_count = {}
    for char in book_content:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_on(dict):
    return dict["count"]
def dic_to_sorted_list(dic):
    sorted_list = []
    for char, count in dic.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list