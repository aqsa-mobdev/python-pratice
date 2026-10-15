password = input("Enter your password: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_number = any(ch.isdigit() for ch in password)

if len(password) >= 8 and has_upper and has_lower and has_number:
    print("Strong Password")
elif len(password) >= 6 and has_lower and (has_upper or has_number):
    print("Moderate Password")
else:
    print("Weak Password")