"""
load the datasets used for the labs in ISLR
see the wonderful https://vincentarelbundock.github.io/Rdatasets/
"""

import pandas as pd

import requests
import io


def download_college():
    """College dataset"""
    college = pd.read_csv(
        io.BytesIO(
            requests.get('http://www-bcf.usc.edu/~gareth/ISL/College.csv').content),
        index_col=0,
        true_values=['Yes'], false_values=['No'])

    return college


def download_auto():
    """Auto dataset"""
    auto = pd.read_csv(
        io.BytesIO(
            requests.get('http://www-bcf.usc.edu/~gareth/ISL/Auto.csv').content),
        na_values=['?'])

    missing = auto[auto.isna().any(axis=1)]
    print('Dropping {} observations with missing data'.format(len(missing)))

    auto = auto.dropna()

    return auto


def download_boston():
    """Housing Values in Suburbs of Boston"""
    boston = pd.read_csv(
        io.BytesIO(
            requests.get('https://vincentarelbundock.github.io/Rdatasets/csv/MASS/Boston.csv').content),
        index_col=0)

    return boston
