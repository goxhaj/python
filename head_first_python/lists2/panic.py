phrase = "Don't panic!"
plist = list(phrase)
print (phrase)
print (plist)

for i in [0, 2, 3, 4, 4, 4, 4, 4]:
    plist.pop(i)
    
plist.insert(2, ' ')
plist.insert(4, 'a')

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
