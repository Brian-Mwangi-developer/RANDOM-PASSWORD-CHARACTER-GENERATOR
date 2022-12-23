import random
import string


def password_Generator(length):
    return ''.join(
        random.choices(
            string.ascii_lowercase + string.digits + string.punctuation +string.ascii_uppercase,k=length
        )
    )
#Choose random characters consisting of digits and letters and takes the parameter k(dictates the length) then (.join) joins to string format
print(password_Generator(8))  #Generate 8 characters
print(password_Generator(12))  #Generate 12 characters
