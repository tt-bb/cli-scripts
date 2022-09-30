sentence = input("Enter your sentence > ")

print("~ Your acronym ~")
for char in sentence.title():
    if char.isupper():
        print(char, end="")
print()
