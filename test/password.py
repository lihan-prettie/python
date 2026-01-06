# 字母數字隨機密碼產生器
import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


print("你的隨機密碼為:", generate_password())


# 含符號大小寫字母和數字的隨機密碼產生器
def generate_string_password(leangth=12):
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    all_char = string.ascii_letters + string.digits + string.punctuation
    password += (random.choice(all_char) for _ in range(leangth - 4))
    random.shuffle(password)
    return "".join(password)


print("你的隨機密碼為:", generate_string_password())
