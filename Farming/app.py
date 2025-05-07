import requests
import numpy as np
import pickle
from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load ML Model
model = pickle.load(open("model_crop.pkl", "rb"))

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://rakshit:smartfarmer@farmer.vqcio.mongodb.net/?retryWrites=true&w=majority&appName=Farmer"
mongo = PyMongo(app)

db = mongo.cx.get_database("Farmer").users  # Ensure correct database reference

# Function to get location from PIN code using API
def get_location_from_pincode(pin_code):
    try:
        response = requests.get(f"https://api.postalpincode.in/pincode/{pin_code}")
        data = response.json()
        if data and data[0]["Status"] == "Success":
            return data[0]["PostOffice"][0]["District"] + ", " + data[0]["PostOffice"][0]["State"]
    except:
        pass
    return "Unknown Location"

# Login Route
@app.route("/", methods=["GET", "POST"])
def index():
    error_message = None  
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            session["user"] = email
            return redirect(url_for("home"))
        else:
            error_message = "Invalid email or password. Please try again."

    return render_template("index.html", error=error_message)

# Signup Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error_message = None  

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        phone = request.form.get("phone")
        pin_code = request.form.get("pin_code")
        location = get_location_from_pincode(pin_code)
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.find_one({"email": email})
        if existing_user:
            error_message = "User already exists! Try logging in."
            return render_template("signup.html", error=error_message)  

        hashed_password = generate_password_hash(password)
        db.insert_one({
            "name": name, 
            "age": age, 
            "phone": phone, 
            "pin_code": pin_code, 
            "location": location, 
            "email": email, 
            "password": hashed_password
        })
        
        return redirect(url_for("index"))

    return render_template("signup.html", error=error_message)

# Home Dashboard Route
@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html")
    return redirect(url_for("index"))

# Crop Prediction Route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        try:
            float_features = [float(x) for x in request.form.values()]
            features = [np.array(float_features)]
            probabilities = model.predict_proba(features)[0]
            crop_probabilities = list(zip(model.classes_, probabilities))
            crop_probabilities.sort(key=lambda x: x[1], reverse=True)
            top_3_crops = [crop_name for crop_name, _ in crop_probabilities[:3]]

            return render_template("predict.html", prediction_text=f"The suitable crops for the land are {', '.join(top_3_crops)}")
        except:
            return render_template("predict.html", prediction_text="Error in processing input values!")

    return render_template("predict.html")

# Profile Page Route
@app.route("/profile")
def profile():
    if "user" in session:
        user = db.find_one({"email": session["user"]})
        return render_template("profile.html", user=user)
    return redirect(url_for("index"))

# Help Page Route
@app.route("/help")
def help():
    return render_template("help.html")

# Logout Route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
