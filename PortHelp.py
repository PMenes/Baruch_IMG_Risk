#!/usr/bin/env python

"""
LIBRARIES AND EXTERNAL PACKAGES
"""
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import time as t
import json

import gspread
import numpy as np
import pandas as pd

"""
AUTHORSHIP INFORMATION 
"""
__author__ = "Baruch Investment Management Group"
__copyright__ = "Copyright (c) 2019 Rajesh R."
__credits__ = ["Rajesh Rao", "Paul Menestrier", "Karol Rychlik"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Baruch Investment Management Group"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"


class PHelper:

    def __init__(self, api_key):
        # data columns present from time series pull by Alpha Vantage API
        self.data_columns = ['1. open', '2. high', '3. low', '4. close', '5. adjusted close',
                             '6. volume', '7. dividend amount', '8. split coefficient']
        self.api_key = api_key

    def stock_puller(self, ticker_list: list, col: str, outputsize: str = 'compact', length: int = 252):
        """
        Extracts stock/security data from Alpha Vantage
        :param ticker_list: a list of tickers for data to be extracted eg: ['SPY', 'GOOG', 'AAPL']
        :param col: provided string to extract the desired column type, illustrated in column_desc list
        :param outputsize: 'compact' = 100 most recent, 'full' = historical security list
        :param length: the number of trading days (from current day) to look back
        :return: returns a dataframe object with relevant time series data (index by date, column ticker symbols)
        """
        big_dict = {}
        ts = TimeSeries(key=self.api_key,
                        output_format='pandas',
                        retries=10)  # function call from Python wrapper to extract time series

        for ticker in ticker_list:
            # iterates through the security list provided and extracts relevant time series information
            data = ts.get_daily_adjusted(symbol=ticker, outputsize=outputsize)[0][col]

            big_dict[ticker] = data[-length:].tolist()  # dictionary storing time series for faster concatenation
            t.sleep(12)

        big_df = pd.DataFrame.from_dict(data=big_dict)  # returns large dataframe for list of securities
        return big_df

    @property
    def sector_puller(self): return SectorPerformances(key=self.api_key,
                                                       output_format='pandas').get_sector()[0]


class GHelper:

    def __init__(self, auth: str):
        self.auth_file = auth

    def google_api(self, wb_name: str):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.auth_file,
                                                                 scope)
        client = gspread.authorize(creds)

        sheet = client.open(wb_name).sheet2

        result = sheet.get_all_records()
        return result

    @property
    def auth_info(self):
        with open(self.auth_file) as f:
            data = json.load(f)
            pprint(data)
        return None


def log_returns(price_df: pd.DataFrame):
    """
    Extracts the log returns for relevant price data
    :param price_df: a dataframe object storing price values for an underlying (index by date, column ticker symbols)
    :return: a dataframe for log returns of select securities
    """
    big_dict = {}

    for ticker in price_df.columns:
        # iterates through the security list provided and extract provided values via dict manipulation
        security_list = price_df[ticker]
        log = np.log(security_list.values) - np.log(np.roll(security_list.values, 1))  # computes log return
        big_dict[ticker] = log[1:].tolist()  # eliminates the first NaN row and returns list from an array

    big_df = pd.DataFrame.from_dict(data=big_dict)  # dataframe index by data column all ticker symbols
    return big_df


def linear_returns(price_df: pd.DataFrame):
    """
    Extracts the linear returns for relevant price data
    :param price_df: a dataframe object storing price values for an underlying (index by date, column ticker symbols)
    :return: a dataframe for linear returns of select securities
    """
    big_dict = {}

    for ticker in price_df.columns:
        # iterates through the security list provided and extract provided values via dict manipulation
        linear_ret = price_df[ticker].pct_change()  # pct_change pandas function for linear returns
        big_dict[ticker] = linear_ret[1:].tolist()  # eliminates the first NaN row and returns list from an array

    big_df = pd.DataFrame.from_dict(data=big_dict)  # dataframe index by data column all ticker symbols
    return big_df


def volatility(price_df: pd.DataFrame, rolling_window: int = 10):
    """
    Extracts the rolling standard deviation of log returns for price data
    :param price_df: a dataframe object storing price values for an underlying (index by date, column ticker symbols)
    :param rolling_window: the length to which rolling standard deviation is taken
    :return: a dataframe for linear returns of select securities
    """
    log_ret = log_returns(price_df)

    big_dict = {}

    for ticker in price_df.columns:
        # iterates through the security list provided and extract provided values via dict manipulation
        vol = log_ret[ticker].rolling(
            rolling_window).std()  # rolling standard deviation pandas function for log returns
        big_dict[ticker] = vol[
                           rolling_window - 1:].tolist()  # eliminates the NaN rows and returns list from an array

    big_df = pd.DataFrame.from_dict(data=big_dict)  # dataframe index by data column all ticker symbols
    return big_df


def sharpe():
    return 1


def sortino():
    return 1


def treynor():
    return 1
