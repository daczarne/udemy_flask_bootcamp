import os
from forms import  AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instanciate the app
app = Flask(__name__)

# Forms keys
app.config["SECRET_KEY"] = "mysecretkey"

# DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app,db)

# Model classes
class Puppy(db.Model):
	# Table name
	__tablename__ = "puppies"
	# Schema
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	# Construtor
	def __init__(self, name):
		self.name = name
	# Repr
	def __repr__(self):
		return f"Puppy name: {self.name}"


# Index
@app.route("/")
def index():
	return render_template("home.html")

# Add
@app.route("/add", methods = ["GET", "POST"])
def add_pup():
	form = AddForm()
	if form.validate_on_submit():
		name = form.name.data
		# Add new Puppy to DB
		new_pup = Puppy(name)
		db.session.add(new_pup)
		db.session.commit()
		return redirect(url_for("list_pup"))
	return render_template("add.html", form = form)


# List
@app.route("/list")
def list_pup():
	# Grab a list of puppies from BD
	puppies = Puppy.query.all()
	return render_template("list.html", puppies = puppies)

# Delete
@app.route("/delete", methods = ["GET", "POST"])
def del_pup():
	form = DelForm()
	if form.validate_on_submit():
		id = form.id.data
		pup = Puppy.query.get(id)
		db.session.delete(pup)
		db.session.commit()
		return redirect(url_for("list_pup"))
	return render_template("delete.html", form = form)

# Run the app
if __name__ == "__main__":
	app.run(debug = True)
