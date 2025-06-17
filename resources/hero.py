from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from models import db

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship(
        'HeroPower',
        backref='hero',
        cascade='all, delete-orphan'
    )

    serialize_rules = ('-hero_powers.hero',)

    def __repr__(self):
        return f"<Hero {self.name} aka {self.super_name}>"
