user_input = input("Enter : ")
user_input_words = user_input.split()

if len(user_input_words) == 1:
    for w in user_input_words:
        count = {}
        for i in w:
            count[i] = count.get(i,0) + 1
        print(f"{w} = {count}")
    max_count = max(count.values())
    for i, j in count.items():
        if j == max_count:
            print(f"Maximum Character Count: {i} {j}")
            break
else:
    for w in user_input_words:
        count = {}
        for i in w:
            count[i] = count.get(i,0) + 1
        print(f"{w} = {count}")
    
    word_count = {}
    for i in user_input:
        if i != " ":
            word_count[i] = word_count.get(i,0) + 1
        
    print(f"{user_input} = {word_count}")

    max_count = max(word_count.values())
    for i, j in word_count.items():
        if j == max_count:
            print(f"Maximum Character Count: {i} {j}")
            break

print("===== End of program =====")