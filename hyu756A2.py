def get_number(num,spaces):
    empty_spaces = spaces - len(str(num))
    final_num = empty_spaces * " " + str(num)
    return str(final_num)

def get_word(words,spaces):
    while len(words) < spaces:
        if (spaces - len(words))%2 == 0:
            empty_spaces = (spaces - (len(words)))//2
            final_words = empty_spaces * " " + str(words) + empty_spaces* " "
        else:
            left_spaces = (spaces - (len(words)))//2 +1
            right_spaces = (spaces - (len(words)))//2
            final_words = left_spaces * " " + str(words) + right_spaces* " "
    while len(words) < spaces:
        final_words = words
    return str(final_words)

def get_row(num,size,spaces):
    for i in range(1,size+1):
        first_part = get_number(i,2)
        if num == 0:
            element = get_number(i,spaces)
            row = first_part + element
        elif len(str(num))== 1:
            element = get_number(num*i,spaces)
            row = first_part + element
        else:
            element = get_number(num*i,spaces)
            row = first_part + element
    return row
def display_separator(size,spaces):
    print("-"*((size+1)*spaces)

def display_table(size,spaces):           
    while num <= size


 
    
def display_heading(size,spaces):
 display_separator(size,spaces)
 title = str(size) + "x" + str(size) + " Times Table"
 print(get_word(title, (size+1)*spaces))
 print(get_row(0, size,spaces))
 display_separator(size,spaces)
          
def main():
 size = get_user_input()
 spaces = len(str(size*size))+2
 display_heading(size,spaces)
 display_table(size,spaces)
 display_separator(size,spaces)
main()
