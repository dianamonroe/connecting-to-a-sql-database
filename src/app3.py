import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import psycopg2


# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
db_engine = create_engine(connection_string).execution_options(autocommit=True)
db_engine.connect()


# 2) TABLES ALREADY CREATED: Execute the SQL sentences to create your tables using the SQLAlchemy's execute function


# 3) DATA ALREADY INSERTED: Execute the SQL sentences to insert your data using the SQLAlchemy's execute function


# 4) Use pandas to print one of the tables as dataframes using read_sql function
# The results can also be stored in a DataFrame and printed as table using Pandas
# Opcion A)
df_books = pd.read_sql_query("SELECT * FROM books", db_engine)
print(df_books)
