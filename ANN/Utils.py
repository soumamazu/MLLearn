"""This module does blah blah."""

from numpy import exp, random

def sigmoid(inp, activation):
    """This method calculates the Sigmoid for the response."""
    return 1 / (1 + exp(- inp / activation))

def random_clamped(size=None):
    """This method returns a random number vector between -1 and 1."""
    random.seed(1)
    return 2 * random.random() - 1 if size is None else 2 * random.random(size) - 1
