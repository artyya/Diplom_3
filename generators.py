from faker import Faker

fake = Faker()


def generate_user_data():
    name = fake.first_name()
    email = f"{name.lower()}@{fake.domain_name()}"
    password = fake.password(length=10)

    return {
        "email": email,
        "password": password,
        "name": name
    }