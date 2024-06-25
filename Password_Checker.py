import re #importing regular expression support module

def checker(p): #checks complexity of password
    length , uppercase, lowercase, num , sp_char = 0 , 0 , 0 , 0 , 0
    if len(p) >= 8: # Check for Minm length (we assume standard required length of 8 characters)
        length = length + 1

    if bool(re.search(r'[A-Z]', p)): # Presence of uppercase letters
        uppercase = uppercase + 1

    if bool(re.search(r'[a-z]', p)): # Presence of lowercase letters
        lowercase = lowercase + 1

    if bool(re.search(r'[0-9]', p)): # Presence of numbers
        num = num + 1

    if bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', p)): # Check for special characters
        sp_char = sp_char + 1

    strength = length + uppercase + lowercase + num + sp_char # Calculate strength

    if strength == 5: # full strength 5
        return "Strong password"
    elif strength >= 3: # strength 3 or 4
        return "Moderately strong password"
    else: # strength 0, 1 or 2
        return "Weak password"

password = input("Enter your password: ")
feedback = checker(password)
print(f"Password strength: {feedback}")
