"""This module does blah blah."""

from numpy import exp

NN_CONFIG = {'iNumInputs': 4, 'iNumOutputs': 2, 'iNumHidden': 1, 'iNeuronsPerHiddenLayer': 6}

def sigmoid(inp, activation):
    """This method calculates the Sigmoid for the response"""
    return 1 / (1 + exp(- inp / activation))
