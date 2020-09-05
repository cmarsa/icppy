# palindrome.py
'''
The code first checks
whether the first and last characters are the same, and if they are goes on to check
whether the string minus those two characters is a palindrome.
'''

def is_palindrome(s):
    '''
    Assumes `s` is a string
    Returns True if the letters in `s` form a palindrome;
        False otherwise. Non-letters and capilatization are ignored.
    '''
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    
    return is_pal(to_chars(s))


def test_is_palindrome():
    word = 'anita lava la tina'
    print('is ' +  '"' + word + '"' + ' a palindrome?')
    print(is_palindrome(word))

    word = 'this is not a palindrome'
    print('is ' +  '"' + word + '"' + ' a palindrome?')
    print(is_palindrome(word))


if __name__ == '__main__':
    test_is_palindrome()