# 1. Import Flask
from flask import Flask


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
  return "All Available Routes"


@app.route("/api/v1.0/precipitation")
def /api/v1.0/precipitation():
    name = "Peleke"
    location = "Tien Shan"

    return f"My name is {name}, and I live in {location}."


@app.route("/contact")
def contact():
    email = "peleke@exple.com"

    return f"Questions? Comments? Complaints? Shoot an email to {email}."


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)