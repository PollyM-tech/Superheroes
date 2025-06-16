from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    # Avoid nesting too deep
    serialize_rules = ('-hero_powers.hero',)

    def __repr__(self):
        return f"<Hero {self.name} aka {self.super_name}>"

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    serialize_rules = ('-hero_powers.power',)

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters.")
        return value

    def __repr__(self):
        return f"<Power {self.name}>"

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        allowed = ['Strong', 'Weak', 'Average']
        if value not in allowed:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'.")
        return value

    def __repr__(self):
        return f"<HeroPower Hero:{self.hero_id} Power{self.power_id} strength={self.strength}>"
