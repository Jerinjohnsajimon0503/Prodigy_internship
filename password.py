import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assessing the strength
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    return strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria

def provide_feedback(strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria):
    feedback = []

    if strength == 5:
        feedback.append("Your password is very strong.")
    elif strength == 4:
        feedback.append("Your password is strong.")
    elif strength == 3:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    return feedback

def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Enter your password: ").strip()
        strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria = assess_password_strength(password)
        feedback = provide_feedback(strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria)
        
        print("\nPassword Strength Feedback:")
        for line in feedback:
            print(f"- {line}")

        again = input("Do you want to check another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Password Strength Checker!")
            break

if __name__ == "__main__":
    main()
