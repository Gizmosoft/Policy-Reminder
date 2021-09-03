def append_string(message1):
    if __name__ == '__append_string__':
        append_string()

    file1 = open("data/message_string.txt","a")      #append
    file1.write(message1 + "\n")
    file1.close()

def clear_file():
    open('data/message_string.txt', 'w').close()

def show_file():
    with open('data/message_string.txt', 'r') as file:
        show_data = file.read()
    return show_data