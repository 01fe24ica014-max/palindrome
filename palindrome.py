def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

if __name__ == "__main__":
    text=input("enter the string:")
    if is_palindrome(text):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
