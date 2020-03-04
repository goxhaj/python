data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print(words)

words2 = [num for num in data if isinstance(num, str)]

print(words)
