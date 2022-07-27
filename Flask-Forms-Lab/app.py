from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
 __name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Polina"
password = "128"
facebook_friends=["Layan","Liraz","Maria", "Joell", "Malak", "Loor"]


@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
 if request.method == 'GET':
 	 return render_template('login.html')
 else:
   name = request.form['username']
   password1 = request.form['password']
   if name=="Polina" and password1 == "128":
     return render_template('home.html', facebook=facebook_friends)
   else:
     return render_template('login.html')


@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friends(name):
	return render_template('friend_exists.html', n=name, facebook=facebook_friends)




if __name__ == "__main__":  # Makes sure this is the main process
 app.run( # Starts the site
  debug=True
	)