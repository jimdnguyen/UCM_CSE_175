#
# main.py
#
# This script provides a top-level driver to exercise some artificial
# neural network code, focusing on learning the Iris classification
# task (which is pretty easy).
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# David Noelle - Mon Nov 15 23:18:16 PST 2021
#

from arch import AnnLinear
from arch import AnnOneHid
from arch import AnnTwoHid
from ann import load_iris_data
from ann import train_model
from ann import test_model
import sys
import pandas as pd


def main():
    # Load the data set ...
    df = pd.DataFrame(columns=["Id", "Model", "Epoch", "Loss"])
    df2 = pd.DataFrame(columns=["Id", "Accuracy"])
    df3 = pd.DataFrame(columns=["Id", "Accuracy"])
    df4 = pd.DataFrame(columns=["Id", "Accuracy"])
    for j in range(0, 25):

        print("DOWNLOADING THE IRIS DATA SET")
        train_in, test_in, train_targ, test_targ = load_iris_data()

        # Create a linear model ...
        model_0hid = AnnLinear()
        # Train the linear model ...
        print("\nTRAINING LINEAR MODEL")
        train_model(model_0hid, train_in, train_targ, j, df)
        # Report test set accuracy ...
        test_accuracy = test_model(model_0hid, test_in, test_targ)
        print(f"Test Set Accuracy = {test_accuracy}")
        df2 = df2.append({"Id": j, "Accuracy": test_accuracy}, ignore_index=True)
        df2.to_csv(
            "./output/AnnLinear_accuracy.csv", mode="a", header=False, index=False
        )
        # Create a model with one hidden layer ...
        model_1hid = AnnOneHid()
        # Train the linear model ...
        print("\nTRAINING MODEL WITH ONE HIDDEN LAYER")
        train_model(model_1hid, train_in, train_targ, j, df)
        # Report test set accuracy ...
        test_accuracy = test_model(model_1hid, test_in, test_targ)
        print(f"Test Set Accuracy = {test_accuracy}")
        df3 = df3.append({"Id": j, "Accuracy": test_accuracy}, ignore_index=True)
        df3.to_csv(
            "./output/AnnOneHid_accuracy.csv", mode="a", header=False, index=False
        )
        # Create a model with two hidden layers ...
        model_2hid = AnnTwoHid()
        # Train the linear model ...
        print("\nTRAINING MODEL WITH TWO HIDDEN LAYERS")
        train_model(model_2hid, train_in, train_targ, j, df)
        # Report test set accuracy ...
        test_accuracy = test_model(model_2hid, test_in, test_targ)
        print(f"Test Set Accuracy = {test_accuracy}")
        df4 = df4.append({"Id": j, "Accuracy": test_accuracy}, ignore_index=True)
        df4.to_csv(
            "./output/AnnTwoHid_accuracy.csv", mode="a", header=False, index=False
        )

    sys.exit(0)


# In PyCharm, press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
