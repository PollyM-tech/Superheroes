from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from resources.hero import Hero
from resources.power import Power
from resources.hero_power import HeroPower
