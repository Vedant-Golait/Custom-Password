import random

# Define the character sets for the password generation
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
lowercase = uppercase.lower()
digits = "0123456789"
symbols =  "!@#$%^&*()V+-="



# Flags to include different character types
upper, lower, nums, syms = True, True, True, True

print("This is a custom strong password Generator") 
print("Note :- The longer you type the letters and Numbers the longer the password gets Type the letters and numbers accordingly ")




# Storing & write Custom name
Name = "Name.txt"
Name_input = input("Enter your Name: ")


with open(Name, 'w') as f:
    f.write(Name_input)


# Storing & Write Custom numbers
Num = "Num.txt"
Num_input = input("Enter your Number: ")

with open(Num, 'w') as f:
    f.write(Num_input)



# Read the user's name from the file
with open(Name, 'r') as f:
    name = f.read().strip()

# Read the user's number from the file
with open(Num, 'r') as f:
    nums = f.read().strip()

# Underscore character used as a separator
r = "_"
v = "@"
# Initialize an empty string to collect all possible characters for the password
all = ""



# Add uppercase letters to the character set if upper is True
if upper:
    all  += uppercase

# Add lowercase letters to the character set if lower is True
if lower:
    all += lowercase

# Add digits to the character set if nums is True
if nums:
    all  += digits

# Add symbols to the character set if syms is True
if syms:
    all  += symbols



# Define the length of the random segments in the password
Length = 4
# Define the number of passwords to generate
Amount = 10

# List to store generated passwords
password = []



# Generate 6 passwords, each containing the user's name and number
for i in range(Amount):
    # Create a password by combining random characters, user name, and number with separators
    password = (random.sample(all, Length) + list(r) + list(name) + list(v) + list(nums) + list(r) + random.sample(all, Length))
    # Convert the list of characters to a string
    password = "".join(password)
    # Print the generated password
    print(password)
    
    # Append the generated password to a file named "passlist.txt"
    with open ("passlist.txt", "a") as f:
        f.write(password  + "\n")
