import sys
from stats import number_of_words, number_of_characters, split_dictionary

print("Usage: python3 main.py <path_to_book>")

#print(sys.argv)

#print(sys.argv("Usage: python3 main.py <path_to_book>", path_to_book=sys.argv[1]))

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def format_list(char_list):
    formatted = ""
    for item in char_list:
        formatted += f"{item['character:']}: {item['count:']}\n"
    return formatted

#print(get_book_text(sys.argv[1]))

#sys.exit(1)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {number_of_words(get_book_text(sys.argv[1]))} total words")
print("--------- Character Count -------")
#print (f"{number_of_characters(get_book_text("sys.argv[1]"))}")
print(format_list(split_dictionary(number_of_characters(get_book_text(sys.argv[1])))))

#print(split_dictionary(number_of_characters(get_book_text("sys.argv[1]"))))