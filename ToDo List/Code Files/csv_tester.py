import csv
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

data = ["abdullah", hash_password("pass")]

with open('credentials.csv', 'a', newline='') as credentials_file:
    writer = csv.writer(credentials_file)
    writer.writeheader()
    writer.writerow(data)