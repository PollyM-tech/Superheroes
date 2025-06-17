# Superheroes API

This is a Flask REST API for managing superheroes and their superpowers. It allows users to view, update, and assign powers to heroes using standard RESTful endpoints.

---

## 🔧 Setup Instructions

1. **Clone the repository**
git clone https://github.com/PollyM-tech/Superheroes.git
cd superheroes
## Create and activate virtual environment

pipenv install
pipenv shell

- Run migrations
flask db init
flask db migrate -m "Initial"
flask db upgrade

- Seed the database
python seed.py

- Run the server
flask run
The app will run on http://127.0.0.1:5555/.

## Testing with Postman
**GET /heroes
Returns a list of all heroes:
http://127.0.0.1:5555/heroes

**GET /heroes/<id>
Returns a single hero with nested hero powers and their associated power info.

Replace <id> with a valid hero ID.
http://127.0.0.1:5555/heroes/1

** GET /powers
Returns all powers:
http://127.0.0.1:5555/powers

**GET /powers/<id>
Replace <id> with a valid power ID.
http://127.0.0.1:5555/powers/1
Returns the specific power or 404 if not found.

** PATCH /powers/<id>
Update a power's description.

{
  "description": "This power allows the user to fly at supersonic speeds."
}
Must be 20+ characters.

Invalid if its too short → returns 400 with:

{
  "errors": ["Description must be at least 20 characters"]
}
** POST /hero_powers
Creates a new relationship between a hero and a power.

{
  "strength": "Average",
  "hero_id": 1,
  "power_id": 2
}
Valid strength: Strong, Average, or Weak

Invalid values return 400 or 404 appropriately.

Returns the updated hero with nested power info.

## File Structure
superheroes/
│
├── app.py                
├── models.py             
├── seed.py               
├── requirements.txt
├── migrations/            
├── resources/           
│   ├── hero.py
│   ├── power.py
│   └── hero_power.py

##  Author
GitHub: PollyM-tech

