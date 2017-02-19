"""This module does blah blah."""

from numpy import dot
from NN import CNeuralNet
from GA import CGenAlg

C = CNeuralNet(3, 1, 2, 1)

# print(len(C.vec_neuron_layers))

# for H in C.vec_neuron_layers:
#     for N in H.vec_neurons:
#         print(N.synaptic_weights)

print(C.get_weights())
# Z = array([[0, 1, 1]])
X = dot(C.get_weights(), -1)

C.put_weights(X)
print(C.get_weights())

print(C.get_number_of_weights())

INPUTS = [1, 1, 1]
print(C.update(INPUTS))

S = CGenAlg(2, 1, 1, 3)
print([pop.weights for pop in S.population])

S.mutate(INPUTS)
print(INPUTS)

SON = []
DAUGHTER = []
MUM = [1, 2, 3, 4, 5, 6]
DAD = [7, 8, 9, 10, 11, 12]
S.crossover(MUM, DAD, SON, DAUGHTER)
print(SON)
print(DAUGHTER)
