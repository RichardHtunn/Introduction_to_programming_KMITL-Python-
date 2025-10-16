user_input = input("Enter : ")
user_input_words = user_input.split()

if len(user_input_words) == 1: # if the user_input has one word
    for w in user_input_words: # to iterate through each words in the input
        count = {}
        for i in w: # to iterate through each letters of every words in the input
            count[i] = count.get(i,0) + 1 # add every letters of each words to the dict
                                          # if the letter(key) is alr in the dict it will add 1 to org letter(key)'s value
                                          # if the letter(key) ain't in the dict it will add both key and value(1) to the dict
        print(f"{w} = {count}")

        max_count = max(count.values()) # put the highest frequent value in "count(dict)" to "max_count(var)"
        for i,j in count.items(): # iterate through "count(dict) items to check which key has the highest frequent value(item)"
            if j == max_count:
                print(f"Maximum Character Count: {i} {j}")
                break
else: # if user_input has more than one word
    for w in user_input_words: # to iterate through each words in the input
        count = {}
        for i in w: # to iterate through each letters of every words in the input
            count[i] = count.get(i,0) + 1 # add every letters of each words to the dict
                                          # if the letter(key) is alr in the dict it will add 1 to org letter(key)'s value
                                          # if the letter(key) ain't in the dict it will add both key and value(1) to the dict
        print(f"{w} = {count}") 

    word_count = {}
    for i in user_input: # this time to iterate through every letters of each word in user_input
        if i != " ":
            word_count[i] = word_count.get(i,0) + 1
    
    print(f"{user_input} = {word_count}")

    max_count = max(word_count.values())
    for i,j in word_count.items():
        if j == max_count:
            print(f"Maximum Character Count: {i} {j}")
            break

print("===== End of program =====")