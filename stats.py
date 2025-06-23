def get_num_words(file):
  return len(file.split())  

def count_characters(file):
  lowered = file.lower() 
  char_counts = {}
  for char in lowered:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts 

def grabnum(e):
  return e['num']

def sort_dic_list(dictionary):
  sort_list = []
  for char in dictionary: 
    sort_list.append({"char": char, "num": dictionary[char]}) 
  sort_list.sort(key=grabnum, reverse=True)
  return sort_list
    
 