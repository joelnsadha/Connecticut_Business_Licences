import pandas as pd
import numpy as np
import requests
import json
from utils import queries


def convert_nonetype(listings):
    """
    Converts any found NoneType data to N/A
    :param listings: List
    :return: List
    """
    converted_listings = []
    # Find any NoneTypes in list & convert to N/A
    for listing in listings:
        all_values = []
        for value in listing:
            value = 'N/A' if value is None else value
            all_values.append(value)
        converted_listings.append(all_values)
    return converted_listings


# Get json data from API
def get_data(filepath):
    """
    Makes API call and retreives data
    :param filepath: API Endpoint. URL
    :return: Json object
    """
    response = requests.get(filepath)
    response_json = response.json()
    return response_json


def process_data(df, con, cur):
    """
    Exports each row in DataFrame to postgres database
    :param df: Pandas DataFrame
    :param con: Psycopg2 database connection
    :param cur: Psycopg2 cursor
    :return: None
    """
    # Convert Nympy integer to Postgres integer
    for index, row in df.iterrows():
        cur.execute(queries.q_ct_business_insert, list(row))
    print('ETL Success!')


# Extract all data into dataframe. There may be missing values. Dataframe will solce this
def process_business(raw_json, con, cur):
    """
    Extracts each field for each business listing within Json object.
    Extracted fields are used to create Pandas DataFrame
    :param raw_json: Json object
    :param con: Psycopg2 Postgres connection
    :param cur: Psycopg2 cursor
    :return: Pandas DataFrame
    """

    listings = []

    # Extract each data field
    for listing in raw_json:
        business_id = listing.get('credentialid')
        name = listing.get('name')
        business_type = listing.get('type')
        credential_code = listing.get('fullcredentialcode')
        credential_type = listing.get('credentialtype')
        credential_number = listing.get('credentialnumber')
        credential = listing.get('credential')
        status = listing.get('status')
        active = listing.get('active')
        issue_date = listing.get('issuedate')
        effective_date = listing.get('effectivedate')
        expiration_date = listing.get('expirationdate')
        address = listing.get('address')
        city = listing.get('city')
        state = listing.get('state')
        zip_code = listing.get('zip')
        record_refreshedon = listing.get('recordrefreshedon')
        status_reason = listing.get('statusreason')
        business_name = listing.get('businessname')
        credential_subcategory = listing.get('credentialsubcategory')
        dba = listing.get('dba')

        # Append extracted data fields to a list. Integer fields are converted.
        listings.append([int(business_id), name, business_type, credential_code, credential_type,
                        credential_number, credential, status, int(active), issue_date,
                        effective_date, expiration_date, address, city, state, zip_code,
                        record_refreshedon, status_reason, business_name, credential_subcategory, dba])

    # Run NoneType converter to convert to N/A
    new_listings = convert_nonetype(listings)

    # Create dataframe
    df = pd.DataFrame(data=new_listings, columns=['business_id', 'name', 'business_type', 'credential_code', 'credential_type',
                                                  'credential_number', 'credential', 'status', 'active', 'issue_date',
                                                  'effective_date', 'expiration_date', 'address', 'city', 'state', 'zip_code',
                                                  'record_refreshedon', 'status_reason', 'business_name', 'credential_subcategory', 'dba'])

    # Return final DataFrame
    return df








