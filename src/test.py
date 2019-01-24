import neural_network as nn
import numpy as np

network = nn.NeuralNetwork([1024, 16, 16, 10])

output = network.feed_forward(np.random.randn(1024, 1))
print(nn.cross_entropy(output, [[0], [1], [0], [0], [0], [0], [0], [0], [0], [0]]))

exit(0)