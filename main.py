def open_file(book_path):
    with open(book_path, 'r') as file:
        text = file.read()
        return text

def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_num = {}
    for char in text.lower():
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
    return char_num

def dict_to_list(char_num):
    char_list = []
    for key, value in char_num.items():
        char_list.append((key, value))
    return char_list
def sort_on(dict_list):
    return sorted(dict_list, key=lambda x: x[1], reverse=True)

def print_report(sorted_list):
    for char, count in sorted_list:
        print(f'The \'{char}\' character was found {count} times')

def main():
    book_path = 'books/frankenstein.txt'
    print(f'--- Begin report of {book_path} ---')
    book = open_file(book_path)
    word_count = (count_words(book))
    print(f'{word_count} words found in the document\n')
    char_num = char_count(book)
    dict_list = dict_to_list(char_num)
    sorted_list = sort_on(dict_list)
    print_report(sorted_list)
    print(f'--- End report ---')

main()
