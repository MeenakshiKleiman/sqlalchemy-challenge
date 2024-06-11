# Climate Data Analysis Project


This project focuses on analyzing climate data, specifically precipitation and temperature observations, using Python and Jupyter Notebook. The analysis includes querying data from a SQLite database, performing statistical calculations, and visualizing the data using histograms.
- Retrieve climate data from a SQLite database
- Perform statistical analysis on temperature and precipitation data
- Generate histograms for data visualization
- Save visualizations as image files

![Precipitation_analysis](https://github.com/MeenakshiKleiman/sqlalchemy-challenge/assets/164884173/e62eb5bb-d220-47fa-a13f-d3e8176f5979)
![Temperature_Observations_Histogram](https://github.com/MeenakshiKleiman/sqlalchemy-challenge/assets/164884173/4b2c35c9-3a94-4758-8de3-84b57d088da5)


# Flask Routes

## /

Start at the homepage.

List all the available routes.

## /api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

## /api/v1.0/stations

Return a JSON list of stations from the dataset.

## /api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

## /api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive
