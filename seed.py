# seed.py

from faker import Faker
from app import app
from models import db, Hero, Power, HeroPower
import random

fake = Faker()

with app.app_context():
    print("Clearing old data...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    print("Seeding powers...")
    powers = [
        Power(name="Flight", description=fake.text(max_nb_chars=60)),
        Power(name="Invisibility", description=fake.text(max_nb_chars=60)),
        Power(name="Telepathy", description=fake.text(max_nb_chars=60)),
        Power(name="Super Strength", description=fake.text(max_nb_chars=60)),
        Power(name="Speed", description=fake.text(max_nb_chars=60)),
    ]
    db.session.add_all(powers)
    db.session.commit()

    print("Seeding heroes...")
    heroes = []
    for _ in range(5):
        hero = Hero(
            name=fake.name(),
            super_name=fake.first_name() + "-" + fake.word().capitalize()
        )
        heroes.append(hero)
    db.session.add_all(heroes)
    db.session.commit()

    print(" Linking heroes with powers...")
    strengths = ["Strong", "Weak", "Average"]
    for hero in heroes:
        for _ in range(2):  # each hero gets 2 powers
            hp = HeroPower(
                hero_id=hero.id,
                power_id=random.choice(powers).id,
                strength=random.choice(strengths)
            )
            db.session.add(hp)
    db.session.commit()

    print("Done seeding!")
