#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# The TA helped me by explaining what the code is suppose to do.
# Denyslon Fuentes helped me understand it by allowing me to talk it out with him.

# ALSO, PROVIDE ANSWERS TO THE FOLLOWING TWO QUESTIONS.
#
# Which network architecture achieves the lowest training set error?
# After running the architecture 25 times, AnnTwoHid had the lowest training set error with 0.024067108

# Which network architecture tends to exhibit the best testing set. accuracy?
# After running the architecture 25 times, AnnOneHid tends to exhibt the best testing set accuracy with an average testing set accuracy of 0.969892473
#
# PLACE YOUR NAME AND THE DATE HERE
# Jim Nguyen 11/17/2021

# PyTorch - Deep Learning Models
import torch.nn as nn
import torch.nn.functional as F


# Number of input features ...
input_size = 4
# Number of output classes ...
output_size = 3


class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layer = nn.Linear(in_features=input_size, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        my_layer_net = self.my_layer(x)
        y_hat = my_layer_net
        return y_hat


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layerin = nn.Linear(in_features=input_size, out_features=20)
        self.my_layerhid1 = nn.Linear(in_features=20, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x1 = self.my_layerin(x)
        x2 = F.relu(x1)
        y_hat = self.my_layerhid1(x2)
        return y_hat


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layerin = nn.Linear(in_features=input_size, out_features=16)
        self.my_layerhid1 = nn.Linear(in_features=16, out_features=12)
        self.my_layerhid2 = nn.Linear(in_features=12, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x1 = self.my_layerin(x)
        x2 = F.relu(x1)
        x3 = self.my_layerhid1(x2)
        x4 = F.relu(x3)
        y_hat = self.my_layerhid2(x4)
        return y_hat
