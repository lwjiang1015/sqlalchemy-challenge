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
        f"/api/v1.0/date/2016-08-23<br/>"
        f"/api/v1.0/date/2016-08-23/2016-12-31"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    prcp = session.query(Measurement.date,Measurement.prcp)\
    .filter(Measurement.date>=(dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    json_dict = {date: value for date, value in prcp}
    
    session.close()
    
    return jsonify(json_dict)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(Station.station, Station.name).all()
    
    session.close() 
    
    return jsonify(list(np.ravel(station_list)))

# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    temperature_most_active_12m = session.query(Measurement.date, Measurement.tobs)\
                .filter(Measurement.station == "USC00519281")\
                .filter(Measurement.date >= (dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    session.close()
    
    return jsonify(list(np.ravel(temperature_most_active_12m)))

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

@app.route("/api/v1.0/date/2016-08-23")
def start_date(date="2016-08-23"):
    print(f"Accept a given start date...")
    
    temp_post_startdate = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
    .filter(Measurement.date >= date).all()
    
    session.close()
    
    return jsonify(list(np.ravel(temp_post_startdate)))

#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/date/2016-08-23/2016-12-31")
def startend(start="2016-08-23",end="2016-12-31"):
    
    print(f"Accept a given start-end range...")
    
    temp_start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
    .filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()
    
    return jsonify(list(np.ravel(temp_start_end)))

if __name__ == '__main__':
    app.run(debug=True)
