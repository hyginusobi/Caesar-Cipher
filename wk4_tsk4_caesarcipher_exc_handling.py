import time


# Function to read file
def read_file(path):
    try: #error handling
        file = open(path, 'r+')
        return file.read()
    except Exception as ex: #error handling
        with open("exceptions.log", "a+") as log:
            log.write(time.strftime("%Y%m%d-%H%M%S") + " Exception occured: " + str(ex) + "\n")
        print("Error: File not found!")
        return False

# Function to write file
def write_file(path, text):
    file = open(path, 'a+')
    return file.write(text)


# Caesar Cipher Algorithm
def caesar_cipher(text, key):
    # Variable to store result of encryption
    encryption = ""

    # Loop through the text
    for x in range(len(text)):
        # cache character
        char = text[x]

        # if character is not an alphabet skip it
        if not (char in "abcdefghijklmnopqrstuvwxyz" or char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            encryption += char
            continue

        # if character is uppercase
        if char.isupper():
            # shifting
            encryption += chr((ord(char) + key - 65) % 26 + 65)
            # otherwise...
        else:
            # small case shifting
            encryption += chr((ord(char) + key - 97) % 26 + 97)

    # return the result
    return encryption


# Function to show all possible key outcomes
def hack_cipher(text):
    for x in range(0, 26):
        result = caesar_cipher(text, 26 - x)
        if x < 10:
            print("Key [0{0}]:".format(x), " ", result)
        else:
            print("Key [{0}]:".format(x), " ", result)


# Function to evaluate each character occurrence in text
def evaluate_text(text):
    # Empty dictionary
    dic_char = {}

    # Iterate through each character
    for x in text:
        # if space don't do anything
        if x == " ":
            continue
        # if already in dictionary
        elif x in dic_char:
            # then increment counter
            dic_char[x] += 1
        else:
            # else add new entry
            dic_char[x] = 1

    return dic_char


# Function to provide main menu and drive all functions
# Contains basic input and output and if statements
def main_loop():
    while 1:
        print("Main Menu")
        print("1. Encrypt text.")
        print("2. Decrypt text.")
        print("3. Encrypt file.")
        print("4. Decrypt file.")
        print("5. Evaluate file.")
        print("6. Hack cipher")
        print("0. Exit")

        user_command = int(input("Enter your command: "))

        if user_command == 1:
            user_text = input("Enter text to encrypt: ")
            user_key = int(input("Enter non-negative shift key number: "))
            result = caesar_cipher(user_text, user_key)
            print("Encrypted text: ", result)
            file_name = "encrypted-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
            write_file(file_name, result)
            print("See file ", file_name, " for output")
        elif user_command == 2:
            user_text = input("Enter text to decrypt: ")
            user_key = int(input("Enter non-negative shift key number : "))
            result = caesar_cipher(user_text, 26 - user_key)
            print("Decrypted text: ", result)
            file_name = "decrypted-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
            write_file(file_name, result)
            print("See file ", file_name, " for output")
        elif user_command == 3:
            user_path = input("Enter file path to encrypt: ")
            user_key = int(input("Enter non-negative shift key number: "))
            result = caesar_cipher(read_file(user_path), user_key)
            print("Encrypted text: ", result)
            file_name = "encrypted-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
            write_file(file_name, result)
            print("See file ", file_name, " for output")
        elif user_command == 4:
            # Request file and key from user
            user_path = input("Enter file path to decrypt: ")
            user_key = int(input("Enter non-negative shift key number: "))
            # Attempt to read file
            text = read_file(user_path)
            # Check if read was successful
            if text != False:
            # If successful, decript file and resume normal execution
                result = caesar_cipher(read_file(user_path), 26 - user_key)
                print("Encrypted text: ", result)
                file_name = "decrypted-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
                write_file(file_name, result)
                print("See file ", file_name, " for output")
            else:
            # If not successful, display additional error message and return to menu choice
                print("Decritpting file failed...")
        elif user_command == 5:
            user_path = input("Enter file path to evaluate: ")
            result = evaluate_text(read_file(user_path))
            for x in result:
                print(x, " ", result[x])
        elif user_command == 6:
            user_text = input("Enter encrypted text to hack: ")
            hack_cipher(user_text)
        elif user_command == 0:
            print("Exiting.")
            break
        else:
            print("Incorrect Command")


main_loop()
