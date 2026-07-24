def check_password_strength(password):
    # 1. Check length requirement (At least 8 characters)
    is_long_enough = len(password) >= 8

    # 2. Check character types using Pythonic approach
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Count how many conditions are met
    passed_checks = sum([is_long_enough, has_uppercase, has_digit, has_symbol])

    # 3. Determine strength result
    if not is_long_enough:
        return "Weak ❌ (Password must be at least 8 characters long)"
    elif passed_checks == 4:
        return "Strong 💪 (All security conditions met)"
    elif passed_checks == 3:
        return "Medium ⚠️ (Add special characters or numbers to make it stronger)"
    else:
        return "Weak ❌ (Include uppercase letters, numbers, and symbols)"


# --- Main Execution ---
if __name__ == "__main__":
    user_password = input("Enter password to check: ")
    result = check_password_strength(user_password)
    print(f"Password Strength: {result}")
