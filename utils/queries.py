# Drops postgres database if it exists
q_drop_database = "DROP DATABASE IF EXISTS ct_business_db;"

# Creates new Postgres database
q_create_database = "CREATE DATABASE ct_business_db WITH ENCODING 'utf8';"

# Drops table
q_drop_ct_business_table = """DROP TABLE IF EXISTS ct_business;"""

# Creates new Postgres table
q_create_table_businsss = """CREATE TABLE ct_business (
    credentialid INT PRIMARY KEY NOT NULL,
    name VARCHAR,
    type VARCHAR,
    fullcredentialcode VARCHAR,
    credentialtype VARCHAR,
    credentialnumber VARCHAR,
    credential VARCHAR,
    status VARCHAR,
    active INT,
    issuedate VARCHAR,
    effectivedate VARCHAR,
    expirationdate VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zip VARCHAR,
    recordrefreshedon VARCHAR,
    statusreason VARCHAR,
    businessname VARCHAR,
    credentialsubcategory VARCHAR,
    dba VARCHAR
);"""

# Inserts data into Postgres table
q_ct_business_insert = """
INSERT INTO ct_business (
    credentialid,
    name,
    type,
    fullcredentialcode,
    credentialtype,
    credentialnumber,
    credential,
    status,
    active,
    issuedate,
    effectivedate,
    expirationdate,
    address,
    city,
    state,
    zip,
    recordrefreshedon,
    statusreason,
    businessname,
    credentialsubcategory,
    dba
)

VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (credentialid) DO UPDATE SET
    name = EXCLUDED.name,
    type = EXCLUDED.type,
    fullcredentialcode = EXCLUDED.fullcredentialcode,
    credentialtype = EXCLUDED.credentialtype,
    credentialnumber = EXCLUDED.credentialnumber,
    credential = EXCLUDED.credential,
    status = EXCLUDED.status,
    active = EXCLUDED.active,
    issuedate = EXCLUDED.issuedate,
    effectivedate = EXCLUDED.effectivedate,
    expirationdate = EXCLUDED.expirationdate,
    address = EXCLUDED.address,
    city = EXCLUDED.city,
    state = EXCLUDED.state,
    zip = EXCLUDED.zip,
    recordrefreshedon = EXCLUDED.recordrefreshedon,
    statusreason = EXCLUDED.statusreason,
    businessname = EXCLUDED.businessname,
    credentialsubcategory = EXCLUDED.credentialsubcategory,
    dba = EXCLUDED.dba;
"""

# Lists of all queries
drop_table_queries = [q_drop_ct_business_table]
create_table_queries = [q_create_table_businsss]
insert_queries = [q_ct_business_insert]
