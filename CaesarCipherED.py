def encrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():
            result += chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a')
            )
        else:
            result += char

    return result


def decrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():
            result += chr(
                (ord(char) - ord('a') - shift) % 26 + ord('a')
            )
        else:
            result += char

    return result


while True:

    print("\n===== CAESAR CIPHER TOOL =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        encrypted = encrypt(text, shift)

        print("Encrypted text:", encrypted)

    elif choice == "2":

        text = input("Enter encrypted text: ")
        shift = int(input("Enter shift value: "))

        decrypted = decrypt(text, shift)

        print("Decrypted text:", decrypted)

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")