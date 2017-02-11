from numpy import random


class SNeuron:
    def __init__(self, numInputs):
        self.numInputs = numInputs
        random.seed(1)
        self.synaptic_weights = 2 * random.random((numInputs + 1, 1)) - 1


class SNeuronLayer:
    def __init__(self, numNeurons, numInputsPerNeuron):
        self.numNeurons = numNeurons
        self.vecNeurons = [SNeuron(numInputsPerNeuron) for count in range(numNeurons)]


class CNeuralNet:
    def __init__(self, numInputs, numOutputs, numHiddenLayers, numNeuronsPerHiddenLayer):
        if numHiddenLayers > 0:
            self.vecNeuronLayers = [SNeuronLayer(numNeuronsPerHiddenLayer, numInputs)]
            for count in range(numHiddenLayers - 1):
                self.vecNeuronLayers.append(SNeuronLayer(numNeuronsPerHiddenLayer, numNeuronsPerHiddenLayer))
            self.vecNeuronLayers.append(SNeuronLayer(numOutputs, numNeuronsPerHiddenLayer))
        else:
            self.vecNeuronLayers.append(SNeuronLayer(numOutputs, numInputs))
    
    def getWeights(self):
        return [weight for layer in self.vecNeuronLayers for neuron in layer.vecNeurons for weight in neuron.synaptic_weights]

    def putWeights(self, weights):
        numWeight = 0
        for i in range(len(self.vecNeuronLayers)):
            for j in range(len(self.vecNeuronLayers[i].vecNeurons)):
                for k in range(len(self.vecNeuronLayers[i].vecNeurons[j].synaptic_weights)):
                    self.vecNeuronLayers[i].vecNeurons[j].synaptic_weights[k] = weights[numWeight]
                    numWeight += 1
        #[[[weights for weight in neuron.synaptic_weights] for neuron in layer.vecNeurons] for layer in self.vecNeuronLayers]