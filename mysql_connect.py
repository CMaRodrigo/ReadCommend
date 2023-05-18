from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine

# Store my credentials in a .env file
load_dotenv('.env') 

# Load the data into dataframes
df_books = pd.read_csv('data/book_details.csv')
df_ratings = pd.read_csv('data/ratings_train.csv')

# Replace the placeholders with your MySQL connection details
username = os.getenv('USER')
password = os.getenv('PASS')
host = os.getenv('HOST')
database_name = os.getenv('DB_NAME')

# Set up the MySQL connection
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database_name}')

# Define schema and table names
schema_name = 'library'
books_table_name = 'books'
ratings_table_name = 'ratings'


# Write the DataFrames to MySQL with the specified schema and table names
df_books.to_sql(books_table_name, con=engine, schema=schema_name, if_exists='replace', index=False)
df_ratings.to_sql(ratings_table_name, con=engine, schema=schema_name, if_exists='replace', index=False)

# Close the MySQL connection
engine.dispose()
