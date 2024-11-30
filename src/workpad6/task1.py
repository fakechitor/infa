def isPalindrome(word : str) -> bool:
    return word == word[::-1]

word = input().lower
print(word)
if isPalindrome(word):
    print("cлово является палиндромом.")
else:
    print("cлово не является палиндромом.")
