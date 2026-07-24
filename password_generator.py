print("="*30)
print(" CODESOFT PASSWORD GENERATOR")
print("="*30)
length=int(input("Enter the length of the password: "))
import random
import string
characters=string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(length):
    password+=random.choice(characters)
print("Generated Password:",)
print(password)