from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

#
VALID_STRENGTHS = ['Strong', 'Average', 'Weak']


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return '<h1>Welcome to the Superheroes API</h1>'


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    response = [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]
    return jsonify(response), 200


@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict(rules=('hero_powers', 'hero_powers.power'))), 200


@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()
    description = data.get('description')

    if not description or len(description) < 20:
        return jsonify({'errors': ['Description must be at least 20 characters']}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict()), 200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if strength not in VALID_STRENGTHS:
        return jsonify({'errors': [f"Strength must be one of: {', '.join(VALID_STRENGTHS)}"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({'errors': ['Hero or Power not found']}), 404

    new_hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify(hero.to_dict(rules=('hero_powers', 'hero_powers.power'))), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)
