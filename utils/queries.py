q_drop_database = "DROP DATABASE IF EXISTS ct_business_db;"
q_create_database = "CREATE DATABASE ct_business_db WITH ENCODING 'utf8'"

q_drop_ct_business_table = """DROP TABLE IF EXISTS ct_business"""

q_create_table_businsss = """CREATE TABLE ct_business (
    credentialid INT NOT NULL,
    name VARCHAR,
    fullcredentialcode VARCHAR,
    credentialtype VARCHAR,
    credentialnumber VARCHAR,
    credential INT,
    status VARCHAR,
    statusreason VARCHAR,
    active INT,
    business.get('issuedate VARCHAR,
    effectivedate VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zip INT,
    recordrefreshedon VARCHAR;
)"""

q_ct_business_insert = """
INSERT INTO ct_business (
    credentialid,
    name,
    fullcredentialcode,
    credentialtype,
    credentialnumber,
    credential,
    status,
    statusreason,
    active,
    issuedate,
    effectivedate,
    address,
    city,
    state,
    zip,
    recordrefreshedon
)

VALUES (%s, %s, %s, %s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s, %s, )

ON CONFLICT(credentialid) DO NOTHING
"""
