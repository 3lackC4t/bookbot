
def get_text():
    with open('/home/blackcat/DevSpace/github.com/3lackC4t/bookbot/books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        return file_contents

def word_count():
    word_list = get_text().split()
    print(len(word_list))

def character_count():
    char_dict = {}
    char_count_list = []
    text_str = get_text().lower()

    def sort_on(dict):
        return dict["num"]

    for char in text_str:
        if char in char_dict and char.isalnum():
            char_dict[char] += 1
        if char not in char_dict and char.isalnum():
            char_dict[char] = 1

    for key in char_dict:
        new_dict = {"char": key, "num": char_dict[key]}
        char_count_list.append(new_dict)

    _sorted = sorted(char_count_list, reverse=True, key=sort_on)
    return _sorted
    

if __name__ == "__main__":
    print(character_count())