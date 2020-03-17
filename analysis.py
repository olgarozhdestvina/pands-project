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
from tabulate import tabulate # for outputting a summary into a table

#importing iris data set, unpaking values of column_names into it as well
raw_data = pd.read_csv('iris.data.txt', names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])

# splitting iris species from the raw_data 
# adapted from https://www.kaggle.com/willvegapunk/iris-data-set
setosa = raw_data[raw_data.Species =="Iris-setosa"]
vesticolor = raw_data[raw_data.Species =="Iris-versicolor"]
virginica = raw_data[raw_data.Species =="Iris-virginica"]

def summ(species):
    species.count()  # Computing count of group
    species.mean()   # Computing mean of groups
    species.median() # Computing median of groups
    species.std()    # Computing standard deviation of groups
    species.mad()    # Returning the mean absolute deviation of the values
    species.var()    # Computing variance of groups
    species.max()    # Computing max of group values
    species.min()    # Computing min of group values
    # Computations and their description taken from https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
    return species.describe()

# information on tabulates was used from https://pypi.org/project/tabulate/
# save the summary for each species into a text file

table = summ(setosa)
with open("Summary.txt", "w") as f: # write into a file
    f.write("<<< Summary for each species of Iris >>> \n\n")    
    #add a table for Setosa
    f.write("\t\t\t\t Iris Setosa \n")
    f.write(tabulate(table, tablefmt="psql", headers = "keys"))

table = summ(vesticolor)
with open("Summary.txt", "a") as f: # append to the same file
    #add a table for Vesticolor
    f.write("\n\n\t\t\t\t Iris Vesticolor \n ")
    f.write(tabulate(table, tablefmt="psql", headers = "keys"))


table = summ(virginica)
with open("Summary.txt", "a") as f:
    #add a table for Virginica
    f.write("\n\n\t\t\t\t Iris Virginica \n")
    f.write(tabulate(table, tablefmt="psql", headers = "keys"))