print(" *** Histogram ***")
fname, word = input("Enter file name and word : ").split()

try:
    fhand = open(fname, 'r')
except:
    print("Error can not open file =>", fname)
    print("===== End of program =====")
    quit()

total_lines = 0
word_count = 0
line_sum = 0
char_counter = {}

for lineno, line in enumerate(fhand, start=1):
    total_lines += 1
    if word in line:
        word_count += line.count(word)
        line_sum += lineno
        for ch in line:
            if ch.isalpha():
                if ch in char_counter:
                    char_counter[ch] += 1
                else:
                    char_counter[ch] = 1

items = []
for k in char_counter:
    items.append((k, char_counter[k]))

def sort_rule(x):
    return (-x[1], -ord(x[0]))

items = sorted(items, key=sort_rule)

top3 = items[:3]

print('Number of "' + word + '" =>', word_count)
print("Sum of line number =>", format(line_sum, ","))
print("Total lines =>", format(total_lines, ","))

for ch, freq in top3:
    freq_str = format(freq, "02")
    spaces = " " * (5 - len(freq_str))
    print(" " + ch + "  => " + "*" * freq + spaces + freq_str)

print("===== End of program =====")
