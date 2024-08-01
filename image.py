from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    encrypted_image = image.copy()
    pixels = encrypted_image.load()

    for i in range(encrypted_image.size[0]):
        for j in range(encrypted_image.size[1]):
            if len(pixels[i, j]) == 4:
                r, g, b, a = pixels[i, j]
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)
            else:
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    decrypted_image = image.copy()
    pixels = decrypted_image.load()

    for i in range(decrypted_image.size[0]):
        for j in range(decrypted_image.size[1]):
            if len(pixels[i, j]) == 4:
                r, g, b, a = pixels[i, j]
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256, a)
            else:
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Welcome to the Image Encryption Tool!")

    while True:
        action = input("Type 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").strip().lower()
        if action in ['encrypt', 'decrypt']:
            break
        print("Invalid input. Please enter 'encrypt' or 'decrypt'.")

    image_path = input("Enter the path to the image file: ").strip()
    output_path = input("Enter the output path for the processed image: ").strip()
    while True:
        try:
            key = int(input("Enter the encryption/decryption key (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    if action == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif action == 'decrypt':
        decrypt_image(image_path, output_path, key)

    again = input("Do you want to process another image? (yes/no): ").strip().lower()
    if again == 'yes':
        main()
    else:
        print("Thank you for using the Image Encryption Tool!")

if __name__ == "__main__":
    main()
