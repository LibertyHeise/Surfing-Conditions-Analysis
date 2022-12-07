# 1. Import Flask
from flask import Flask, jsonify


# 2. Create an app
app = Flask(__name__)

# 3. Dictionaries

precip_dict = 
station_dict = 
temp_dict = 
specifics_dict = 

# 4. Define static routes
@app.route("/")
def index():
  return f"All Available Routes\
  precipitation_analysis\
  stations_analysis\
  temp_observations\
  specific_start_data\
  specific_start_end_data"


@app.route("/api/v1.0/precipitation")
def precipitation_analysis():
    return f"Here is the JSON representation of the dictionary."


@app.route("/api/v1.0/stations")
def stations_analysis():
    return f"Here is the JSON list of stations."
    
@app.route("/api/v1.0/tobs")
def temp_observations():
    return f"Here is a JSON list of temp obs. for the previous year."
    
@app.route("/api.v1.0/<start>")
def specific_start_data():
    return f"JSON list of all minimum, avg, max temps"

@app.route("/api/v1.0/<start>/<end>")
def specific_start_end_data():
    return f"specifics"


# 5. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
