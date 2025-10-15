def get_sort_key(item):
    return (item[1], item[0])

def analyze_file(filename, word):
    file = None
    try:
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()

        word_count = 0
        line_number_sum = 0
        total_lines = len(lines)
        relevant_lines_content = ""

        for i, line in enumerate(lines):
            line_number = i + 1
            if word in line:
                word_count += line.count(word)
                line_number_sum += line_number
                relevant_lines_content += line

        most_common_chars = []
        if relevant_lines_content:
            char_counts = {}
            for char in relevant_lines_content:
                if 'a' <= char <= 'z':
                    char_counts[char] = char_counts.get(char, 0) + 1
            
            if char_counts:
                items_list = list(char_counts.items())
                most_common_chars = sorted(items_list, 
                                           key=get_sort_key, 
                                           reverse=True)
        
        print(f'Number of "{word}" => {word_count}')
        print(f'Sum of line number => {line_number_sum:,}')
        print(f'Total lines => {total_lines:,}')
        
        max_asterisk_len = 0
        if most_common_chars:
            max_asterisk_len = most_common_chars[0][1]

        for char, count in most_common_chars[:3]:
            asterisks = '*' * count
            print(f" {char}  => {asterisks:<{max_asterisk_len}} {count:02d}")
        
    except FileNotFoundError:
        print(f"Error can not open file => {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    try:
        print(" *** Histogram ***")
        user_input = input("Enter file name and word : ")
        parts = user_input.split()
        
        if len(parts) >= 2:
            input_filename = parts[0]
            input_word = " ".join(parts[1:])
            analyze_file(input_filename, input_word)
            print("===== End of program =====")
        else:
            print("Invalid input: Please enter a filename and a word, separated by a space.")

    except (EOFError, IndexError):
        print("Invalid input format. Please try again.")
    except Exception as e:
        print(f"An error occurred during input: {e}")

