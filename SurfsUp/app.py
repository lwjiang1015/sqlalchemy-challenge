# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`

Base = automap_base()

# Use the Base class to reflect the database tables

Base.prepare(autoload_with=engine)

Base.classes.keys()

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to SurfsUp Hawaii!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/starttoend"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    """Return json with the date as the key and the value as the precipitation"""
    """Only return json the jsonified precipitation data for the last year in the database"""

    precipitation_one_year = session.query(Measurement.date,Measurement.prcp)\
    .filter(Measurement.date>=(dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    def Convert(precipitation_one_year):
        prcp_dict = {'date': 'prcp'}
    
    return jsonify(prcp_dict)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(Station.station, Station.name).all()
    return jsonify(station_list)

# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    temperature_most_active_12m = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.station == "USC00519281").\
                filter(Measurement.date >= (dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    return jsonify(temperature_most_active_12m)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

@app.route("/api/v1.0/<start>")
def start(date):
    temp_post_startdate = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
    .filter(Measurement.date >= (dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    return jsonify(temp_post_startdate)

#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    start_date = dt.date(2017,8,23)-dt.timedelta(days=365)
    end_date = dt.date(2016,12,31)
    temp_start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs,func.max(Measurement.tobs)))\
    .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
    return jsonify(temp_start_end)


if __name__ == '__main__':
    app.run(debug=True)
