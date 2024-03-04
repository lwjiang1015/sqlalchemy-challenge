# sqlalchemy-challenge
module 10 challenge

# Analyse and explore the climate data


## Use the file climate_starter.ipynb and perform the following tasks:

### Jupyter note book database connection including:

    Use the SQLAlchemy create_engine() function to connect to your SQLite database

    Use the SQLAlchemy automap_base() function to reflect your tables into classes

    Save references to the classes named Station and Measurement 

    Link Python to the database by creating a SQLAlchemy session

    Close the session

### Conducted Precipitation Analysis including: 

    Create a query that finds the most recent date in the dataset (8/23/2017) 

    Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable

    Save the query results to a Pandas DataFrame to create date and precipitation columns

    Sort the DataFrame by date 

    Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables

    Use Pandas to print the summary statistics for the precipitation data 

### Conducted Station Analysis including:

    Design a query that finds the number of stations in the dataset (9)

    Design a query that lists the stations and observation counts in descending order and finds the most active station (USC00519281) 

    Design a query that finds the min, max, and average temperatures for the most active station (USC00519281) 

    Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations

    Save the query results to a Pandas DataFrame 

    plot a histogram with bins=12 for the last year of data using tobs as the column to count. 

### Coding for API SQLite Connection & Landing Page using the file provided as a starter, including:


    Generate the engine to the sqlite file

    Use automap_base() and reflect the database schema

    Save references to the tables in the sqlite file (measurement and station)

    Create and binds the session between the python app and database 

    Displayed the available routes on the landing page 

Specifically, for API Static Routes 

    Returns json with the date as the key and the value as the precipitation

    Only returns the jsonified precipitation data for the last year in the database

    generate a stations route that:

    Returns jsonified data of all of the stations in the database 

    generage a tobs route that:

    Returns jsonified data for the most active station (USC00519281) 

    Only returns the jsonified data for the last year of data

    generate the API Dynamic Route that:

    Accepts the start date as a parameter from the URL 

    Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset 

    generate a start/end route that:

    Accepts the start and end dates as parameters from the URL 

    Returns the min, max, and average temperatures calculated from the given start date to the given end date

    For the coding Conventions and Formatting 

    Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. 

    Name functions and variables with lowercase characters, except for the naming of the datasets "Measurement" and "Station" as indicated in the starter codes, with words separated by underscores. 

    Endeavour to follow DRY (Don't Repeat Yourself) principles

    Attempt to use concise logic and creative engineering where possible

For the Deployment and Submission 

Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. 

Use the command line to add your files to the repository. 

Include appropriate commit messages in the files. 


## References/acknowledgement
This assignment has been completed primarily with reference to the course materials for Module 10. The help from the teaching team, the tutor, and from the Xpert Learning Assistant at Datacampspot are acknowledged. 



