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
    var = species.var()       # Computing variance of groups
    mx = species.max()        # Computing max of group values
    mn = species.min()        # Computing min of group values
    # Computations and their description taken from https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html

    # adding space to structure output, rounding computations to 2 decimal places
    # information on spacing was adapted from https://pyformat.info/

    space = "\t\t\t  {:^20}{:^15}{:^15}{:^15}"
    specs_space = '{:30}{:^15.2f}{:^15.2f}{:^15.2f}{:^15.2f}'

    # evaluate to an iterable (adapted from https://dimitrisjim.github.io/python-unpackings-unpacked.html)
    print("\n")
    print(species.name)
    print(space.format(*column_names))
    print(specs_space.format("Count", *count.values))
    print(specs_space.format("Mean", *mean.values))
    print(specs_space.format("Median", *median.values))
    print(specs_space.format("Standard Deviation", *std.values))
    print(specs_space.format("Mean Absolute Deviation", *mad.values))
    print(specs_space.format("Variance", *var.values))  
    print(specs_space.format("Min", *mn.values))
    print(specs_space.format("Max", *mx.values))
    species.describe()

# print the summary for each species 
 
summ(setosa)
summ(vesticolor)
summ(virginica)

