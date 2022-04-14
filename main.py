import pdb
import re

# read text file
test_file_dir = "./test.txt"
f = open(test_file_dir, "r")
lines = f.readlines()
f.close()

all_numbers_list = []
for line in lines:
    # extract numbers within []
    extract_list_in_line = re.findall("\[([^]]+)", line)

    # split numbers
    for extract in extract_list_in_line:
        # "," style
        if "," in extract:
            extract_split_list = list(map(int, extract.split(",")))
            all_numbers_list += extract_split_list

        # "–" style. This is en-dash, different from hyphen.
        if "–" in extract:
            start, end = list(map(int, extract.split("–")))
            extract_split_list = [*range(start, end + 1)]  # include end number
            all_numbers_list += extract_split_list

        # single citation number
        if extract.isdigit():
            all_numbers_list += [int(extract)]

        # empty -> skip that case

unique_all_numbers_list = sorted(list(set(all_numbers_list)))  # find unique and sort.
print(unique_all_numbers_list)
for number in unique_all_numbers_list:
    print(number)
