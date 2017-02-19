"""This module contains the basic structural units of the Neural Network."""

from Utils import sigmoid, random_clamped

class SNeuron:
    """This class is a Single Neuron."""
    def __init__(self, numInputs):
        self.num_inputs = numInputs
        self.synaptic_weights = random_clamped(numInputs + 1)


class SNeuronLayer:
    """This class is a Single Neuron Layer."""
    def __init__(self, numNeurons, numInputsPerNeuron):
        self.num_neurons = numNeurons
        self.vec_neurons = [SNeuron(numInputsPerNeuron) for count in range(numNeurons)]


class CNeuralNet:
    """This class is the Complete Neural Network."""
    def __init__(self, numInputs, numOutputs, numHiddenLayers, numNeuronsPerHiddenLayer):
        self.num_inputs = numInputs
        self.num_hidden_layers = numHiddenLayers
        if numHiddenLayers > 0:
            self.vec_neuron_layers = [SNeuronLayer(numNeuronsPerHiddenLayer, numInputs)]
            self.vec_neuron_layers.extend([SNeuronLayer(numNeuronsPerHiddenLayer,
                                                        numNeuronsPerHiddenLayer)
                                           for count in range(numHiddenLayers - 1)])
            self.vec_neuron_layers.append(SNeuronLayer(numOutputs, numNeuronsPerHiddenLayer))
        else:
            self.vec_neuron_layers = [SNeuronLayer(numOutputs, numInputs)]

    def get_weights(self):
        """This method returns all the weights as a single vector."""
        return [weight for layer in self.vec_neuron_layers for neuron in layer.vec_neurons
                for weight in neuron.synaptic_weights]

    def put_weights(self, weights):
        """This method assigns all the weights from a single vector."""
        num_weight = 0
        for i in range(len(self.vec_neuron_layers)):
            for j in range(len(self.vec_neuron_layers[i].vec_neurons)):
                for k in range(len(self.vec_neuron_layers[i].vec_neurons[j].synaptic_weights)):
                    self.vec_neuron_layers[i].vec_neurons[j].synaptic_weights[k] = weights[num_weight]
                    num_weight += 1

    def get_number_of_weights(self):
        """This method returns the number of weights."""
        return len(self.get_weights())

    def update(self, inputs):
        """This method calculates the output vector given an input vector."""
        outputs = []
        if len(inputs) != self.num_inputs:
            return outputs
        for i in range(self.num_hidden_layers + 1):
            if i > 0:
                inputs = outputs
            inputs.append(-1)
            outputs = [sigmoid(sum([j * k for j, k in zip(neuron.synaptic_weights, inputs)]), 1)
                       for neuron in self.vec_neuron_layers[i].vec_neurons]
        return outputs
