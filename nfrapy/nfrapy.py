"""Main module."""

from __future__ import absolute_import, division, print_function, unicode_literals

import urllib.request
import json
import pandas as pd

# The base URL to access the NFRA API
BASE_URL = "https://nrfaapps.ceh.ac.uk/nrfa/ws"

VALID_DATA_TYPES = [
    'gdf', 'ndf', 'gmf', 'nmf', 'cdr', 'cdr-d', 'cmr',
    'pot-stage', 'pot-flow', 'gauging-stage', 'gauging-flow',
    'amax-stage', 'amax-flow'
]

def catalogue():
    """
    This gets the data catalog from nfra an returns it as a pandas dataframe
    You can use this dataframe to get station characteristics
    

	Returns:
		pandas Dataframe containing the National Flow Record Archive catalog, which has metadata about all stations

	Author: Simon Moulds
	Date: 20/01/2024
	"""
    
    query = "station=*&format=json-object&fields=all"
    stations_info_url = "{BASE}/station-info?{QUERY}".format(
        BASE=BASE_URL, QUERY=query
    )

    # Send request and read response
    response = urllib.request.urlopen(stations_info_url).read()

    # Decode from JSON to Python dictionary
    response = json.loads(response)
    df = pd.DataFrame(response['data'])
    return df


def _build_ts(response):
    """
    This is used to parse timeseries data from the nfra
    
    Args:
        response (json):  this is a json that is parsed from a bitstream provided by the nfra API

	Returns:
		pandas Dataframe containing the requested dataset

	Author: Simon Moulds
	Date: 20/01/2024
	"""
    variable = response['data-type']['id']
    dates = response['data-stream'][0::2]
    values = response['data-stream'][1::2]
    df = pd.DataFrame.from_dict({'time': dates, variable: values})
    return df


def get_ts(id, data_type):
    """
    This gets a timeseries from the National Flow Record Archive
    
    Args:
        id (int): an integer value for a station 
        data_type (str): A string describing the data type you want. Options are: 'gdf', 'ndf', 'gmf', 'nmf', 'cdr', 'cdr-d', 'cmr', 'pot-stage', 'pot-flow','gauging-stage', 'gauging-flow','amax-stage', 'amax-flow' The details of these options can be found at https://nrfa.ceh.ac.uk/data-formats-types
        

	Returns:
		pandas Dataframe containing the requested dataset

	Author: Simon Moulds
	Date: 20/01/2024
	"""
    query = "station=" + str(id) + "&data-type=" + data_type + "&format=json-object"
    stations_info_url = "{BASE}/time-series?{QUERY}".format(
        BASE=BASE_URL, QUERY=query
    )

    # Send request and read response
    response = urllib.request.urlopen(stations_info_url).read()

    # Decode from JSON to Python dictionary
    response = json.loads(response)

    df = _build_ts(response)
    return df
