def caesar_cipher(text, shift, direction):
    result = ""
    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        while True:
            direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").strip().lower()
            if direction in ['encrypt', 'decrypt']:
                break
            print("Invalid input. Please enter 'encrypt' or 'decrypt'.")

        message = input("Enter your message: ").strip()
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        result = caesar_cipher(message, shift, direction)
        print(f"The resulting message is: {result}")

        again = input("Do you want to encrypt/decrypt another message? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Caesar Cipher Program!")
            break

if __name__ == "__main__":
    main()
