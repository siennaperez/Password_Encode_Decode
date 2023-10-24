# Sienna Perez's file with partner Andrew Sawarynski
def encoder(password):  # encodes password
    encoded_password = ''
    for digit in password:
        new_number = str((int(digit) + 3) % 10)  # adds 3 to each digit
        encoded_password += new_number
    return(encoded_password)

def decoder(encoded_password):
    pass


while __name__ == "__main__":
    # main menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    # user input for the password
    menu_selection = int(input("Please enter an option: "))

    # encoder selection
    if menu_selection == 1:
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")

    # decoder selection
    if menu_selection == 2:
        print(f"The encoded password is {encoder(password)}, and the original password is {password}.")

    # quit selection
    if menu_selection == 3:
        break