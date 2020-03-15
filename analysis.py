# Olga Rozhdestvina
# This program  is a part of the project on Fisher's Iris Data Set
# It outputs a summary of each variable to a single text ﬁle,
# saves a histogram of each variable to png ﬁles, 
# outputs a scatter plot of each pair of variables to png files

# importing libraries
import pandas as pd # for data analysis and manupulation
import numpy as np # for plotting
import seaborn as sns # for plotting
import matplotlib.pyplot as plt # for plotting

# making a list of column names for the future table
column_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

#importing iris data set, unpaking values of column_names into it as well
raw_data = pd.read_csv('iris.data.txt', header=None, names = [*column_names, "Species"])

# grouping raw data by species
grouped = raw_data.groupby(["Species"])

# constructing each iris species from grouped raw data 
setosa = grouped.get_group("Iris-setosa")
setosa.name = "Iris Setosa" # applying name attribute 
vesticolor = grouped.get_group("Iris-versicolor")
vesticolor.name = "Iris Vesticolor"
virginica = grouped.get_group("Iris-virginica")
virginica.name = "Iris Virginica"



def summ(species):
    count = species.count()   # Computing count of group
    mean = species.mean()     # Computing mean of groups
    median = species.median() # Computing median of groups
    std = species.std()       # Computing standard deviation of groups
    mad = species.mad()       # Returning the mean absolute deviation of the values
    corr = species.corr()     # Computing pairwise correlation of columns
    var = species.var()       # Computing variance of groups
    cov = species.cov()       # Computing pairwise covariance of columns
    mx = species.max()        # Computing max of group values
    mn = species.min()        # Computing min of group values
    # Computations and their description taken from https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html


# evaluate to an iterable (adapted from https://dimitrisjim.github.io/python-unpackings-unpacked.html)
    print(species.name)
    print(*column_names)
    print("Count", *count.values)
    print("Mean", *mean.values)
    print("Median", *median.values)
    print("Standard Deviation", *std.values)
    print("Mean Absolute Deviation", *mad.values)
    print("Pairwise Correlation", *corr.values)
    print("Variance", *var.values)
    print("Coefficient of Variation", *cov.values)    
    print("Min", *mn.values)
    print("Max", *mx.values)
    species.describe()
    
summ(setosa)
summ(vesticolor)
summ(virginica)

