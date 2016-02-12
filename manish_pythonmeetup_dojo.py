#! user/bin/python
import re
fp1 =  open("input_file.txt", 'r')

fread = fp1.read()

fread_norm = re.sub(r'[\s\t]+', " ", re.sub(r'[^a-zA-Z0-9]', " ", fread)).lower()

word_list = fread_norm.split(" ")

word_count_dict = {}
for word in word_list:
	try:
		got_word = word_count_dict[word]
	except KeyError:
		word_count_dict[word] = 1
	else:
		word_count_dict[word] += 1
		
for key, value in word_count_dict.items():
	print key, value


