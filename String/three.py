print(" *** Kebab string ***")
user_input = input("Enter some words: ").split()

words = []
for i in user_input:
    words.append(i.lower())

kebab_case = "-".join(words)

print(f"Kebab-case => {kebab_case}")
print("===== End of program ======")