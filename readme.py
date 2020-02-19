print("####################################")
print("This project contains python scripts")
print("####################################")

with open('README.md') as file:
    for line in file:
        print(line, end='')