import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(12)])

print(f"Your random password is: {password}")
