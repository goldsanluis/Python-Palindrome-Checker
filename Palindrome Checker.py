def is_palindrome(text):
    """Check if a string is a palindrome, ignoring spaces and case."""
    if not isinstance(text, str):
        return False
    
    cleaned = ""
    for char in text.lower():
        if char.isalpha():
            cleaned = cleaned + char
    
    return cleaned == cleaned[::-1]

print(is_palindrome("Ghani"))
print(is_palindrome("Regina"))
print(is_palindrome("Gold"))
print(is_palindrome("Bernal"))
print(is_palindrome("San"))
print(is_palindrome("Luis"))
print(is_palindrome("Aba! Babababa ba?"))
print(is_palindrome("Anak, ama ka na."))
print(is_palindrome("Anak, nasa'n ka na."))
print(is_palindrome("Ano na"))
print(is_palindrome("Nasa bayabasan"))
print(is_palindrome("O! tatayo yata 'to."))