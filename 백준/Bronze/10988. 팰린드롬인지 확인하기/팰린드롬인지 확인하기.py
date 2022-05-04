word = input()


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(1 if is_palindrome(word) else 0)