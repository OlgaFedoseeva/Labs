import pybrain
from pybrain.tools.shortcuts import buildNetwork

net = buildNetwork(2, 3, 1)
print(net.activate([2, 1]))
print(net['in'])
print(net['hidden0'])
print(net['out'])
