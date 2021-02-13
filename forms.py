from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange, EqualTo, AnyOf, DataRequired

species = ['cat', 'dog', 'porcupine', 'Cat', 'Dog', 'Porcupine']


class AddPet(FlaskForm):

    name = StringField("Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    species = StringField("Species", validators=[
        InputRequired(message="Species cannot be blank"), AnyOf(species, message="Must be dog, cat, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField('Available')
    submit = SubmitField("Submit")


class EditPet(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField('Available')
