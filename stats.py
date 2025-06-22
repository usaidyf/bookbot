def get_no_words(text):
   return len(text.split())

def get_no_chars(text):
   text = text.lower()
   char_counts = {}
   for char in text:
      if char in char_counts:
         char_counts[char] += 1
      else:
         char_counts[char] = 1
   return char_counts

def get_char_counts_in_list(char_counts):
   result = []
   for char, count in char_counts.items():
      result.append({"char": char, "num": count})
      
   result.sort(key=lambda x: x["num"], reverse=True)
   return result