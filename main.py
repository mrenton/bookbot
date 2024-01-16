def main():
    path_to_file = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_file} ---")
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(f"The book in path {path_to_file} has {num_words} words")
    num_chars = get_num_chars(text)
    char_list = create_sorted_list_from_dict(num_chars)
    
    for letter in char_list:
        print(f"The '{letter}' character was found {num_chars[letter]} times")
    print(f"--- End report of {path_to_file} ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
     words = text.split()
     return len(words)

def get_num_chars(text):
    char_count_dict = {}
    words = text.split()
    for word in words:
        lowercase_word = word.lower()
        for letter in lowercase_word:
            if letter in char_count_dict:
                char_count_dict[letter] += 1
            else: 
                char_count_dict[letter] = 1

    return char_count_dict

def create_sorted_list_from_dict(dict):
    key_list = []
    for key in dict:
        if key.isalpha():
            key_list.append(key)
    
    key_list.sort()
    return key_list




main()
