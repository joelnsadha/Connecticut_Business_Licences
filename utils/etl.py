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
    df = pd.read_json(raw_json)
    for index, row in df.iterrows():
        # Convert Nympy integer to Postgres integer
        int_row = [int(value) if isinstance(value, np.int64) else value for value in row]
        cur.execute(queries.q_ct_business_insert, int_row)

