from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "My name"
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
