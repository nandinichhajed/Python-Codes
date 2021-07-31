# You are given words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification.

# If the following string is given as input to the program:
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Then, the output of the program should be:
# 3
# 2 1 1

# Hints
# Make a list to get the input order and a dictionary to count the word frequency

# Code
n = int(input("Enter no of word and words:"))

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')
