# Phonepe Pulse Data Visualization
-- PhonePe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly


# Work Done in Jupiter Notebook
  -- PhonePe pulse data are fetched using Git Clone from PhonePe's Repo
  -- All the fetched data are in JSOM format. So the Data are converted to Data Frame using Pandas library.
  -- The converted data are then converted to CSV format and downloaded to local environment.

# SQL Part
  -- Six different tables are created in SQL as required to push the Data in CSV file.


# Python Part
  -- Now the CSV file is fetched from the local environment to Python and then converted to Data Frame.
  -- The files converted to Data Frame are then moved to SQL using insert query and PostgreSQL connection.
  
  Streamlit :-
   -- In Streamlit the visualizations and presentations are done using Plotly in python.
         Visualization is done in map using Chorapleth.
   -- When a combination of options are selected in Streamlit in the front end, accordingly code and query is 
         run in the back end to fetch data from SQL and conversion processing is done in the python environment 
         and visual representation is made in the front end in streamlit interface.
    
