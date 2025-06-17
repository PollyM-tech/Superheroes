from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from models import db

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship(
        'HeroPower',
        backref='power',
        cascade='all, delete-orphan'
    )

    serialize_rules = ('-hero_powers.power',)

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters.")
        return value

    def __repr__(self):
        return f"<Power {self.name}>"
