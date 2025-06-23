from stats import get_num_words,count_characters, sort_dic_list
import sys

def get_book_text(filepath):
  with open(filepath) as f: 
    return f.read()
  return "Error"

def main():
  if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_path = sys.argv[1]
  num_words = get_num_words(get_book_text(book_path))
  letters = count_characters(get_book_text(book_path))
  sorted_list = sort_dic_list(letters)

  print("============ BOOKBOT ===========\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_list:
    if(item['char'].isalpha()):
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")


main()