from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """ Form for adding new pets """
    pet_name = StringField("Pet name", 
                validators=[InputRequired()])
    species = StringField("Species", 
                validators=[InputRequired()])
    photo_url = StringField("Photo URL", 
                validators=[Optional(), URL(require_tld=True)])
    age = IntegerField("Age", 
                validators=[InputRequired()], coerce=int)
    notes = TextAreaField("Notes")