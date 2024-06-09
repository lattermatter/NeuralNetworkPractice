inputs_to_neuron = [6, -.5, 5]
weights_connections = [1, 2.2, -0.5]
bias = 3

output = 0
for i in range(len(inputs_to_neuron)):
    output += inputs_to_neuron[i] * weights_connections[i]

output += bias
print(output)
