#1 Enter a string of words separated by spaces. Find the longest word.
def longest_word():
    x = input('Please enter your string: ')
    words = x.lower().split()
    print(words)
    words.sort(key=len)
    return words[-1]

#2 Enter an irregular string
def irregular():
    x = input('Please enter your irregular string: ')
    words = x.split()
    regular = " ".join(words)
    print(regular)

#3 Count times a character is included in a string. NO METHOD COUNT
def char_count():
    x = input('Please enter your string: ')
    all_chars = list(x.lower())
    print(all_chars)
    y = input('What character do you want to count: ').lower()
    count = 0
    char_check = ''
    for item in all_chars:
        if str(y) == str(item):
            count += 1
            char_check = str(y)
    return char_check, count

#4 Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings. No replace
def replace_string():
    x = input('Please input your string: ').lower()
    replaced = input('Please input the substring of what you want replaced: ').lower()
    replaced_by = input('Please input the substring of what to replace it with: ').lower()
    full_string = x.split()
    for i, word in enumerate(full_string):
        if replaced in full_string:
            full_string[i] = replaced_by
    print(' '.join(full_string))


##print(longest_word())
##irregular()
##print(char_count())
replace_string()