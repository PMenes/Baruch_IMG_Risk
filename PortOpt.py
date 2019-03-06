#!/usr/bin/env python

"""
LIBRARIES AND EXTERNAL PACKAGES
"""
import numpy as np


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


def mbp(cov: np.matrix, mu: np.array):
    """
    Minimum variance portfolio Given target return, determine the weights of the portfolio with the smallest variance
    :param cov: provided covariance matrix for the underlying securities (np.matrix object)
    :param mu: expected returns/historical returns for underlying securities (np.array object)
    :return: a dict containing the weights of the provided portfolio
    """
    base = np.ones(len(mu[0]))
    inv = np.linalg.inv(cov.values)

    weights = (inv.dot(base)) / (base.dot(inv).dot(base))
    exp_return = (mu.dot(inv).dot(base)) / (base.dot(inv).dot(base))

    return weights, exp_return


def mpo(cov: np.matrix, mu: np.array, risk_free: float):
    """
    Market Portfolio Optimization Given target return, determine the weights of the optimal market portfolio
    :param cov: provided covariance matrix for the underlying securities (np.matrix object)
    :param mu: expected returns/historical returns for underlying securities (np.array object)
    :param risk_free: current risk_free rate in 10 year bonds
    :return: a dict containing the weights of the provided portfolio
    """
    assert 0 < risk_free < 1

    base = np.ones(len(mu[0]))
    inv = np.linalg.inv(cov.values)

    weights = ((mu - risk_free * base).dot(inv)) / ((mu - risk_free * base).dot(inv).dot(base))

    return weights


def quad():
    """
    Portfolio Optimization (Quadratic Programming)
    :return: a dict containing the weights of the provided portfolio
    """
    return 1
