import random
from faker import Faker

from data.data import People, Person

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield People(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def create_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 100),
        salary=random.randint(1000, 100000),
        department=faker_ru.job(),
    )


def generated_file():
    path = rf'/Users/proarea/Desktop/filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path
