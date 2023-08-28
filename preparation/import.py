import asyncio

# import time
from random import choice

from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from social_media.core import init_db
from social_media.core.database import engine
from social_media.tables import User
from social_media.tables.enums import Gender

HOBBIES = [
    "Reading books",
    "Blogging",
    "Dancing",
    "Singing",
    "Listening to music",
    "Playing musical instruments (piano, guitar etc.)",
    "Learning new languages",
    "Shopping",
    "Traveling",
    "Hiking",
    "Cycling",
    "Exercising",
    "Drawing",
    "Painting",
    "Collecting things",
    "Playing computer games",
    "Cooking",
    "Baking",
    "Gardening",
    "Doing crafts (handmade)",
    "Embroidering",
    "Sewing",
    "Knitting",
    "Playing board games",
    "Walking",
    "Writing stories",
    "Fishing",
    "Photography",
    "Skydiving",
    "Skating",
    "Skiing",
    "Roller skating",
    "Longboarding",
    "Surfing",
]
faker = Faker()


def prepare_data(line) -> dict:
    fullname, age, city = line.strip().split(",")
    last_name, first_name = fullname.split(" ")
    user = {
        "uuid": faker.uuid4(),
        "first_name": first_name,
        "second_name": last_name,
        "age": int(age),
        "gender": Gender.female.value if last_name[-1] == 'а' else Gender.male.value,
        "hobby": choice(HOBBIES),
        "city": city,
        "password": "$2b$12$tKxaF7j0GYlkfpug7vjL9.Mg7aD5ns6T8IHngdPzzrcH3DD8fSXiy",
    }

    return user


async def parse_data(limit=10000):
    await init_db()
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as main_session:
        with open("people.csv", 'r') as file:
            lines = file.readlines()
            if not lines:
                return

            start, end = 0, limit
            parts_count = int(len(lines) / limit)
            for i in range(parts_count):
                users = []
                # start_time = time.time()
                for index in range(start, end):
                    users.append(prepare_data(lines[index]))
                # middle_time = time.time()
                await main_session.run_sync(
                    lambda session: session.bulk_insert_mappings(User, users)
                )
                await main_session.commit()
                # insert_time = time.time()
                # print(f"Duration PARSER: ", middle_time - start_time)
                # print(f"Duration DB: ", insert_time - middle_time)
                print(f"Committed {limit} users: {start}, {end}")
                start, end = end, end + limit

            await main_session.commit()


if __name__ == "__main__":
    asyncio.run(parse_data())
