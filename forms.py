from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """ Form for adding new pets """
    pet_name = StringField("Pet name", 
                validators=[InputRequired()])
    species = SelectField('Species',
                choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", 
                validators=[Optional(), URL(require_tld=True)])
    age = IntegerField("Age",
                validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """ Form for editing pets """
    photo_url = StringField("Photo URL", 
                validators=[Optional(), URL(require_tld=True)])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")