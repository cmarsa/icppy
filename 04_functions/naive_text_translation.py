# naive_text_translation.py

en_to_fr = {
    'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'Je',
    'eat': 'mange', 'drink': 'bois', 'John': 'Jean',
    'friends': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge'
}

fr_to_en = {
    'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
    'mange':'eat', 'bois':'drink', 'Jean':'John',
    'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'
}

dicts = {'EN to FR': en_to_fr, 'FR to EN': fr_to_en}

def translate_word(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


def translate(phrase, dicts, direction):
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    letters = upper_case + lower_case
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation + translate_word(word, dictionary) + c
            word = ''
    return translation + translate_word(word, dictionary)


def test_translate():
    print(translate('I drink good red wine, and eat bread.', dicts, 'EN to FR'))
    print(translate('Je_bois_du vin_rouge.', dicts, 'FR to EN'))


if __name__ == '__main__':
    test_translate()

'''
Not all types of of objects can be used as keys: A key must be an object of a
hashable type. A type is hashable if it has
* A __hash__ method that maps an object of the type to an int , and for every ob-
ject the value returned by __hash__ does not change during the lifetime of the
object, and
* An __eq__ method that is used to compare objects for equality.

All of Python’s built-in immutable types are hashable, and none of Python’s
built-in mutable types are hashable. It is often convenient to use tuples as keys.

'''