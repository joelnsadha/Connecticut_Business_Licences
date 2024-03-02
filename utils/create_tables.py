import psycopg2
from utils import queries


def create_database():
    """
    Creates Postgres Database. Connects to default database & creates new database.
    Connection is closed for the defauled database and a new connection is made to the new database
    returning a connection & cursor
    :return: con [connection to new database], cur [psycopg2 cursor for new database]
    """
    # Make connection to default Postgres databse.
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=Summer2024@")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Drop databse if exists
    cur.execute(queries.q_drop_database)

    # Create new database
    cur.execute(queries.q_create_database)

    # Close connection
    conn.close()

    # Connect to newly created database
    conn = psycopg2.connect("host=127.0.0.1 dbname=ct_business_db user=postgres password=Summer2024@")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return conn, cur


def create_tables(conn, cur):
    """
    Creates tables in Postgres databse
    :param conn: Psycopg2 Postgres databse connection
    :param cur: Psycopg2 cursor
    :return: None
    """
    # Run drop table queries to drop any tables
    for query in queries.drop_table_queries:
        cur.execute(query)

    # Run create table queries to create new tables
    for create_query in queries.create_table_queries:
        cur.execute(create_query)




