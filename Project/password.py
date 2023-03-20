import random
import secrets
import string

letters = string.ascii_lowercase
cletters = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

alphabet = letters + cletters + digits + special_chars

pwd_length = 12

pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print(pwd)



