from faker import Faker

def generate_meme_data():
    fake = Faker()
    return {
        "text": fake.sentence(),
        "url": fake.url(),
        "tags": [fake.word() for _ in range(3)],
        "info": {"author": fake.first_name()}
    } 