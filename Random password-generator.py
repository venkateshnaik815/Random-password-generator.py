import random
import string

chars = "abcdfghiklmnopqrstuvwxyzABCDFGHIJKLMOPQRSTUVWXYZ123456@#$%^^&*([{"

password_len = int(input("what lenght would you like your password to be:"))
password_count = int(input("How many passowrd would u like:"))

password = password_len + password_count

for x in range(0,password_count):
    print(x)

password_count=""

for i in range(0,password_len):
    password_char = random.choice(chars)
    password      =      password_char
    print(password_char)

print("here is your password:" , password)


