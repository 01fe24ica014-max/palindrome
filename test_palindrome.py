from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("madam")==True
def test_not_palindrome():
    assert is_palindrome("python")==False
def test_values():
    assert is_palindrome("121")==True