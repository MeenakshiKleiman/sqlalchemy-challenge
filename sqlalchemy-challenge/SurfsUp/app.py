# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an app
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# Create an engine for the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the SQL-Alchemy APP API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )

# Route for precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()
    
    # Create a dictionary from the row data and append to a list
    all_precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_precipitation.append(prcp_dict)

    return jsonify(all_precipitation)

# Route for stations data
@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station, Station.name).all()
    
    # Convert list of tuples into normal list
    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)

    return jsonify(all_stations)

# Route for temperature observations
@app.route("/api/v1.0/tobs")
def tobs():
    # Query temperature observations for the most active station
    most_active_station = session.query(Measurement.station).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).first().station
    
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.station == most_active_station).all()
    
    # Create a list of temperature observations
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

# Route for temperature statistics from the start date
@app.route("/api/v1.0/<start>")
def start(start):
    # Query min, avg, and max temperatures for all dates >= start date
    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).all()
    
    temp_stats = []
    for min, avg, max in results:
        temp_stats_dict = {}
        temp_stats_dict["min"] = min
        temp_stats_dict["avg"] = avg
        temp_stats_dict["max"] = max
        temp_stats.append(temp_stats_dict)

    return jsonify(temp_stats)

# Route for temperature statistics for a date range
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query min, avg, and max temperatures for all dates between start and end date
    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).\
              filter(Measurement.date <= end).all()
    
    temp_stats = []
    for min, avg, max in results:
        temp_stats_dict = {}
        temp_stats_dict["min"] = min
        temp_stats_dict["avg"] = avg
        temp_stats_dict["max"] = max
        temp_stats.append(temp_stats_dict)

    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run(debug=True)
