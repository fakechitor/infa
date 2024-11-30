AMOUNT_OF_WORDS_IN_ARRAY = 5
words = []
for i in range(AMOUNT_OF_WORDS_IN_ARRAY):
    words.append(input())
print(words)
print(list(map(len, words)))