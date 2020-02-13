def search4vowels(phrase:str) -> set:
    """ Retun any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    for vowel in found:
        print (vowel)

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """return a set of the 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))
