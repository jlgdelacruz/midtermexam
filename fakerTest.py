from faker import Faker

fake = Faker()

print("Generating fake data:")
print()

for _ in range(10):
    fullName = fake.name()
    emailAdd = fake.email()
    jobTitle = fake.job()
    companyName = fake.company()

    print(f"Name: {fullName}")
    print(f"Email: {emailAdd}")
    print(f"Job Title: {jobTitle}")
    print(f"Company Name: {companyName}")
    print()