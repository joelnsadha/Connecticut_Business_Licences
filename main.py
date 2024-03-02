# Import modules
from utils import create_tables
from utils import etl

# Api Endpoint
filepath = "https://data.ct.gov/resource/ngch-56tr.json"

# Get response from API Endpoint
json_response = etl.get_data(filepath)

# Create database connection & cursor for Postgres
con, cur = create_tables.create_database()

# Create Pandas DataFrame
df = etl.process_business(raw_json=json_response, con=con, cur=cur)

if __name__ == '__main__':
    # Create tables in database
    create_tables.create_tables(con, cur)

    # Load data into database
    etl.process_data(df=df, con=con, cur=cur)

    # Close connection
    con.close()

