def get_num_words(book):
    list_of_words = book.split()
    num_words=len(list_of_words)
    print(f"Found {num_words} total words")

def get_letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_char(char_dict):
    char_list = []
    for items in char_dict:
        tmp = {"char": items, "num": char_dict[items]}
        char_list.append(tmp)
    char_list.sort(reverse=True,key=sort_on)
    return char_list