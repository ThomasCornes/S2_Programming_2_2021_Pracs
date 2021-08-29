"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

count_of_word = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = count_of_word.get(word, 0)
    count_of_word[word] = frequency + 1

words = list(count_of_word.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, count_of_word[word]))