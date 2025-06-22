import sys
from stats import get_no_words, get_no_chars, get_char_counts_in_list

def get_book_text(file_path):
   with open(file_path) as f:
      return f.read()
   
def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
      
   file_path = sys.argv[1]   
   
   text = get_book_text(file_path)
   no_of_words = get_no_words(text)
   no_of_chars = get_no_chars(text)
   char_counts_list = get_char_counts_in_list(no_of_chars)

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print("----------- Word Count ----------")
   print(f"Found {no_of_words} total words")
   print("--------- Character Count -------")
   
   for char_info in char_counts_list:
      if char_info['char'].isalpha():
         print(f"{char_info['char']}: {char_info['num']}")

   print("============= END ===============")

main()