full_name = input("Enter your full name: ")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

initials = first_name[0] + last_name[0]

print("First Name:", first_name)
print("Last Name:", last_name)
print("Initials:", initials)
print("Uppercase Name:", full_name.upper())
print("Reversed Name:", full_name[::-1])