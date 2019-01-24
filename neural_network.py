import numpy as np


class NeuralNetwork:
    def __init__(self, sizes):
        self.sizes = sizes
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]

    def feed_forward(self, a):
        """Return the output of the network if "a" is input activations."""
        for b, w in zip(self.biases, self.weights):
            a = leaky_relu(np.dot(w, a) + b)

        return a


def leaky_relu(weighted_sum):
    """Returns weightedSum if weightedSum > 0, otherwise 0.01"""
    logit = []

    for i in range(len(weighted_sum)):
        logit.append(abs(weighted_sum[i]) * (weighted_sum[i] > 0) + ((weighted_sum[i] < 0) * 0.01))

    return logit


def softmax(logit):
    """Distributes all values in a vector into a range from [0, 1]"""
    exps = np.exp(logit - np.max(logit))

    return exps / np.sum(exps)


def cross_entropy(logit, labels):
    """Calculates cost of neural network using cross entropy. Closer the cost is to 0 the better."""
    probabilities = softmax(logit)

    print(probabilities)
    print(labels)

    return -np.sum(labels * np.log(probabilities))
