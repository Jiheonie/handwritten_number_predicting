import load_mnist
import network
from layers import DenseLayer, ActivationLayer

training_data, test_data = load_mnist.load_data() 

net = network.SequentialNetwork() 

net.add(DenseLayer(784, 392))  
net.add(ActivationLayer(392))
net.add(DenseLayer(392, 196))
net.add(ActivationLayer(196))
net.add(DenseLayer(196, 10))
net.add(ActivationLayer(10))  

# <1> First, load training and test data.
# <2> Next, initialize a sequential neural network.
# <3> You can then add dense and activation layers one by one.
# <4> The final layer has size 10, the number of classes to predict.


net.train(training_data, epochs=10, mini_batch_size=10,
          learning_rate=3.0, test_data=test_data)