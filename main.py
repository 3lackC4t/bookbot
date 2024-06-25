import re

def main():
    with open('/home/blackcat/DevSpace/github.com/3lackC4t/bookbot/books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        return file_contents

def word_count():
    word_list = main().split()
    print(len(word_list))

def character_count():
    character_hash = {}
    for char in list(main().lower()):
        if char in character_hash and char != " ":
            character_hash[char] += 1
        else:
            character_hash[char] = 1
    
    return character_hash



if __name__ == "__main__":
    char_hash = character_count()
    for char in char_hash:
        print(f"{char}: {char_hash[char]}")