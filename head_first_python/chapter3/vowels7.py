vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in sorted(list(found)):
    print (vowel)
