from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import json
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

config = {
  "apiKey": "AIzaSyBSZBOwpX2T3jOQL7OH8gHe6PHHuKP0XA8",
  "authDomain": "geonius-1f1b3.firebaseapp.com",
  "databaseURL": "https://geonius-1f1b3-default-rtdb.firebaseio.com",
  "projectId": "geonius-1f1b3",
  "storageBucket": "geonius-1f1b3.appspot.com",
  "messagingSenderId": "108528968724",
  "appId": "1:108528968724:web:1f3039a49174346dc9b301",
  "measurementId": "G-LR9PCMF8Z9",
  "databaseURL": "https://geonius-1f1b3-default-rtdb.firebaseio.com/"
} 

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        
        try:
            login_session["user"] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('map'))
        except:
            return render_template("signin.html")

    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]

        try:
            login_session["user"] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {'username':username, 'email':email, 'password':password}
            db.child('Users').child(UID).set(user)
            return redirect(url_for('map'))
        except:
            return render_template("signup.html")

    return render_template("signup.html")

@app.route('/map', methods = ["GET", "POST"])
def map():
    if request.method ==  "POST":
        UID = login_session['user']['localId']
        final_score = request.form["jsvar"]
        print(final_score)
        return render_template('map.html')
    return render_template('map.html')





if __name__ == '__main__':
    app.run(debug=True, port=5001)