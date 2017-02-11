from numpy import dot, array
from NN import CNeuralNet

C = CNeuralNet(3, 1, 2, 3)

for H in C.vecNeuronLayers:
    for N in H.vecNeurons:
        print N.synaptic_weights
        
print C.getWeights()
Z = array([[0, 1, 1]])
X = dot(C.getWeights(), 2)

C.putWeights(X)
print C.getWeights()