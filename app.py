from flask import Flask, render_template, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests

from models import connect_db, db, Pet, DEFAULT_IMG_URL 
from forms import AddPetForm, EditPetForm

from secrets import PET_FIND_API_KEY, PET_FIND_API_SECRET

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbfhsigdfyua'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)

PET_FIND_URL=f'http://api.petfinder.com/pet.getRandom?format=json&key={PET_FIND_API_KEY}&output=basic'

@app.route("/")
def show_homepage():
    """ Shows all pets """

    pets = Pet.query.all()

    random_pet_data = get_random_pet()

    return render_template("index.html", pets=pets, random_pet=random_pet_data)


def get_random_pet():
    random_p_jsn = requests.get(PET_FIND_URL)
    random_pet = random_p_jsn.json()

    name = random_pet['petfinder']['pet']['name']['$t']
    age = random_pet['petfinder']['pet']['age']['$t']
    
    try:
        photo_url = random_pet['petfinder']['pet']['media']['photos']['photo'][3]['$t']
    except KeyError:
        photo_url = DEFAULT_IMG_URL

    random_pet_data = {
        'name': name,
        'age': age,
        'photo_url': photo_url
    }
    return random_pet_data

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Show and handle add pet form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None

        new_pet = Pet(name=name, 
                    species=species, 
                    photo_url=photo_url, 
                    age=age, 
                    notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template(
            "add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """ Show and handle edit pet form """

    # finding pet and and prepopulate form
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data or None
        pet.notes = form.notes.data or None
        pet.available = form.available.data
        
        db.session.commit()

        return redirect("/")
    else:
        # Re-present form for editing
        return render_template(
            "edit_pet_form.html", form=form, pet=pet)
