import pandas as pd
import numpy as np
import requests
import json
from utils import queries


def get_data(filepath):
    response = requests.get(filepath)
    response_json = response.json()
    return response_json


def process_business_data(raw_json, con, cur):
    businesses = []
    converted = []
    for biz in raw_json:
        business_values = []
        for key, value in biz.items():
            business_values.append(value)
        businesses.append(business_values)

    # Convert Nympy integer to Postgres integer
    for business in businesses[0]:
        converted_business = [int(value) if isinstance(value, np.int64) else value for value in business]
        converted.append(converted_business)

    cur.execute(queries.q_ct_business_insert, converted)


# Extract all data into dataframe. There may be missing values. Dataframe will solce this
def process_business(raw_json, con, cur):
    listings = []
    for listing in raw_json:
        listings.extend([listing.get('credentialid'), listing.get('name')])

    # Create dataframe
    print(listings)




