import sys

def get_book_text(x):
        y = x.split()
        z = len(y)
        return z

def countChar(x):
	char_low = str.lower(x)
	char_list = list(char_low)
	char_dict = {}
	for char in char_list:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	print(char_dict)

def charSorted(x):
	char_low = str.lower(x)
	char_list = list(char_low)
	char_dict = {}
	final_list = []
	final_lists = []
	for char in char_list:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	char_lists = list(char_dict.items())
	for i in range (0, len(char_lists)-1):
		temp_list = list(char_lists[i])
		final_list.append({"char": temp_list[0], "num": temp_list[1]})
		
	final_list.sort(reverse=True, key=sort_on)
	return final_list

def sort_on(items):
	return items['num']


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	with open(sys.argv[1]) as f:
		file_contents = f.read()
	word_count = get_book_text(file_contents)
	char_count = charSorted(file_contents)
	print_report(sys.argv[1], word_count, char_count)
	


main()
