from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from models import db

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Average', 'Weak']:
            raise ValueError("Strength must be 'Strong', 'Average', or 'Weak'.")
        return value

    def __repr__(self):
        return f"<HeroPower Hero:{self.hero_id} Power:{self.power_id} Strength:{self.strength}>"
