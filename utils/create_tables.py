import psycopg2
from . import queries


def create_database():
    # Make connection to default Postgres databse.
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=Summer2024@")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Drop databse if exists
    cur.execute(queries.q_drop_database)
    cur.execute(queries.q_create_database.format('ct_business_db'))

    # Close connection
    conn.close()

    # Connect to ct_business_db database
    conn = psycopg2.connect("host=127.0.0.1 dbname=ct_business_db user=postgres password=Summer2024@")
    cur = conn.cursor()
    return conn, cur


def create_tables():
    pass

