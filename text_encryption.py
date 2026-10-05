text = input("Enter your text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = ""

for char in text:

    if char.isalpha():

        encrypted_text += chr(
            (ord(char) - ord('a') + shift) % 26 + ord('a')
        )

    else:

        encrypted_text += char

print("Encrypted text:", encrypted_text)