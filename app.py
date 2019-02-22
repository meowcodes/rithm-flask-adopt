FROM flask IMPORT Flask, request, render_template, redirect, jsonify
FROM flask_wtf IMPORT FlaskForm
FROM wtforms IMPORT StringField
FROM wtforms.validators IMPORT DataRequired
FROM flask_debugtoolbar IMPORT DebugToolbarExtension

FROM models IMPORT Pet

app = Flask(__name__)
app.config['SECRET_KEY' ]= 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tarot_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)