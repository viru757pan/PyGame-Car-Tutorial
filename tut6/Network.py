import random
from utils import lerp


class NeuralNetwork:
    def __init__(self, neuronCounts):
        self.levels = []
        for i in range(len(neuronCounts)-1):
            self.levels.append(Level(neuronCounts[i], neuronCounts[i+1]))

    def feedForward(givenInputs, network):
        outputs = Level.feedForward(givenInputs, network.levels[0])
        for i in range(1, len(network.levels)):
            outputs = Level.feedForward(outputs, network.levels[i])

        return outputs

    @staticmethod
    def mutate(network, amount=1):
        for i, level in enumerate(network.levels):
            level.biases = [lerp(bias, random.random() * 2 - 1, amount)
                            for bias in level.biases]

            level.weights = [[lerp(weight, random.random() * 2 - 1, amount)
                              for weight in row] for row in level.weights]

    def to_json(self):
        json_data = {
            'levels': []
        }
        for level in self.levels:
            json_level = {
                'inputs': level.inputs,
                'outputs': level.outputs,
                'biases': level.biases,
                'weights': level.weights
            }
            json_data['levels'].append(json_level)
        return json_data

    @staticmethod
    def from_json(json_data):
        neuron_counts = [len(json_data['levels'][0]['inputs'])]
        for json_level in json_data['levels']:
            neuron_counts.append(len(json_level['outputs']))
        network = NeuralNetwork(neuron_counts)
        for i, json_level in enumerate(json_data['levels']):
            level = network.levels[i]
            level.inputs = json_level['inputs']
            level.outputs = json_level['outputs']
            level.biases = json_level['biases']
            level.weights = json_level['weights']
        return network


class Level:
    def __init__(self, inputCount, outputCount):
        self.inputs = [None] * inputCount
        self.outputs = [None] * outputCount
        self.biases = [None] * outputCount

        self.weights = [[None] * outputCount for _ in range(inputCount)]

        self.randomize()

    def randomize(self):
        for i in range(len(self.inputs)):
            for j in range(len(self.outputs)):
                self.weights[i][j] = random.random() * 2 - 1

        for i in range(len(self.biases)):
            self.biases[i] = random.random() * 2 - 1

    @staticmethod
    def feedForward(givenInputs, level):
        for i in range(len(level.inputs)):
            level.inputs[i] = givenInputs[i]

        for i in range(len(level.outputs)):
            sum = 0
            for j in range(len(level.inputs)-1):
                sum += level.inputs[j] * level.weights[j][i]
            level.outputs[i] = 1 if sum > level.biases[i] else 0

        return level.outputs
