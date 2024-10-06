from collections import defaultdict 
from operator import itemgetter


def read_text_from_txt(file1):
  with open(file1, 'r', encoding="utf-8") as f1: text1 = f1.read().strip()

  return text1


def mapper(file, separator=' '): 
  data = read_text_from_txt(file)
  words = data.split(separator)
  mapped_data = [(word, 1) for word in words] 
  print(f"Mapped data from {file}", mapped_data, "\t") 
  return mapped_data


def shuffler(mappers_output): 
  shuffle_store = defaultdict(list) 
  for mapper_output in mappers_output:
    for word, count in mapper_output: 
      shuffle_store[word].append(count)

  print("Shuffle store:", dict(shuffle_store)) 
  return shuffle_store


def sort_shuffled_output(shuffled_data):
  return sorted(shuffled_data.items(), key=itemgetter(0))


def reducer(sorted_data, separator=' '):
  print("Counted words:")
  for word, counts in sorted_data: 
      total_count = sum(counts)
      print(f"{word}{separator}{total_count}")


def main():
  files = ['text1test.txt', 'text2test.txt', 'text3test.txt']
  mappers_output = [mapper(file) for file in files] 
  shuffled_data = shuffler(mappers_output) 
  sorted_data = sort_shuffled_output(shuffled_data) 
  reducer(sorted_data)

if __name__ == "__main__": main()


