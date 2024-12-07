def isPalindrome(word : str) -> bool:
    word.lower()
    return word == word[::-1]

print(isPalindrome("aba"))
print(isPalindrome("adad"))