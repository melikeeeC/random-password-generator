import random, string

length = int(input("Şifre uzunluğunu gir: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print("Oluşturulan şifre:", password)