import psycopg2
from utils.create_tables import create_database, create_tables
from utils import etl

# Api Endpoint
filepath = "https://data.ct.gov/resource/ngch-56tr.json"

# Get response from API Endpoint
json_response = etl.get_data(filepath)

# Postgres connection & cursor
con, cur = create_database()

if __name__ == '__main__':
    # Create tables in database
    #create_tables(con, cur)

    # Execute ETL process
    #etl.process_business_data(raw_json=json_response, con=con, cur=cur)

    # Test
    etl.process_business(raw_json=json_response, con=con, cur=cur)

    # Close connection
    #con.close()

