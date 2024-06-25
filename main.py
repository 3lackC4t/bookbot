import argparse
import os


class BookBot:
    def __init__(self, path = '', text = ''):
        self.path = os.path.abspath(path)
        with open(self.path, 'r') as f:
            self.text = f.read()

    def set_path(self, new_path) -> None:
        self.path = os.path.abspath(new_path)

    def get_path(self) -> str:
        return self.path

    def word_count(self) -> int:
        word_list = self.text.split()
        return len(word_list)

    def character_count(self) -> list[dict]:
        char_dict = {}
        char_count_list = []
        text_str = self.text.lower() 

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

    def print_form(self):
        print(f"--- Begin report of {self.path} ---")
        print(f"{self.word_count} words in this document")
        print("\n\n")
        for char_dict in self.character_count():
            print(f"The {char_dict["char"]} character was found {char_dict["num"]} times")

        print("--- End report ---")

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', 
                        type=str, 
                        action='store',
                        help='the path to the text file you will be using')

    args = parser.parse_args()
    return args

def main():
    args = build_parser()
    new_book = BookBot(args.path)
    new_book.print_form()

if __name__ == "__main__":
    main()