import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
station = Base.classes.station

#Flask Setup

app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
  return (
    f"Welcome to the Precipitation App!<br>"
    f"All Available Routes:<br>"
    f"/api/v1.0/precipitation<br>"
    f"/api/v1.0/stations<br>"
    f"/api/v1.0/tobs<br>"
    #f"/api.v1.0/<start><br>"
    #f"/api/v1.0/<start>/<end><br>"
  )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    """Return a list of last year's precipitation"""
    # Query 
    Precip_DF = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    #Convert list of tuples into normal list
    all_dates = list(np.ravel(Precip_DF))

    return jsonify(all_dates)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """Here is the JSON list of stations"""

    #Query
    total_number_stations= session.query(station.station).all()
    
    session.close()

    #Convert list of tuples into normal list
    all_stations = list(np.ravel(total_number_stations))

    return jsonify(all_stations)
    
@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    """JSON list of temp obs. for the previous year"""

    #Query
    active_stations = session.query(Measurement.station,
    func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    b_station = active_stations[0][0]
    query_date = dt.date(2017,8,23)-dt.timedelta(days=365)
    temp_obs = session.query(Measurement.station, Measurement.tobs).\
    filter(Measurement.station == b_station).\
    filter(Measurement.date >= query_date).all()
    
    session.close()

    #Convert list of tuples into normal list
    year_temps = list(np.ravel(temp_obs))

    return jsonify(year_temps) 


# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
