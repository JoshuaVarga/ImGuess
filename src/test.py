import neural_network as nn
import numpy as np
import cifar as cf
import matplotlib.pyplot as plt
from tkinter import *

# network = nn.NeuralNetwork([1024, 16, 16, 10])

# output = network.feed_forward(np.random.randn(1024, 1))
# print(nn.cross_entropy(output, [[0], [1], [0], [0], [0], [0], [0], [0], [0], [0]]))
root = Tk()

photo = PhotoImage(file="test.png")

arr = np.asarray(photo)
arr2 = arr.tolist()
print(arr2)
label = Label(root, image=photo)
label.pack()

root.mainloop()