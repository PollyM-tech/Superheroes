# superheroes API

This is a flask REST API for managing superheroes and their superpowers.

# Setup Instructions 
1. Clone repository

bash
git clone https://github.com/PollyM-tech/Superheroes.git
cd superheroes

2.  Create a virtusl environment
pipenv install
pipenv shell

3. run migrations 
flask db init   
flask db migrate -m "Initial"
flask db upgrade

4. Seed the Database
python seed.py

5. Run the server 
flask run

# Testing with Postman
- GET /heroes
Returns a list of all heroes with their ID, name, and super name.

- GET /heroes/<id>
Returns a hero with nested hero powers and their associated power info.
Replace :id with a valid hero ID from the previous response.


- GET /powers
Should return all seeded powers with id, name, and description.

- GET /powers/<id>
Replace :id with a valid power ID.
Should return that specific power or 404 if not found.

- PATCH /powers/<id>
Try updating a power’s description with valid/invalid strings.
20+ chars → success.
short → should return 400 with error message.
*** Requires: JSON body with description (min 20 characters)

- POST /hero_powers
Body (JSON):
{
  "strength": "Average",
  "hero_id": 1,
  "power_id": 2
}

Should create the relationship and return the updated hero (with new power).
Invalid strength or bad IDs → return appropriate 400 or 404.





