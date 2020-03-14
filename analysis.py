# Olga Rozhdestvina
# This program  is a part of the project on Fisher's Iris Data Set

# It outputs a summary of each variable to a single text ﬁle,
# saves a histogram of each variable to png ﬁles, 
# outputs a scatter plot of each pair of variables to png files

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

raw_data = pd.read_csv('iris.data.txt', header=None)
raw_data.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

def summ(iris):
    print("Summary for ")