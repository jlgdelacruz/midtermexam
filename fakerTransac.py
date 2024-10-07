from faker import Faker
import random

fake = Faker()

print("Generating fake data:")
print()

for _ in range(10):
    transactionID = fake.name()
    transactionDate = fake.past_date()
    amountNum = round(random.uniform(100,500),2)

    print(f"ID: {transactionID}")
    print(f"Date: {transactionDate}")
    print(f"Amount: {amountNum}")
    print()