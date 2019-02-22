from flask import Flask, request, render_template, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY' ]= 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route("/")
def show_homepage():
    """ Shows all pets """

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """ Show and handle add pet form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template(
            "add_pet_form.html", form=form)