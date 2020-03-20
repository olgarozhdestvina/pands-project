# Olga Rozhdestvina
# This program  is a part of the project on Fisher's Iris Data Set
# It outputs a summary of each variable to a single text ﬁle,
# saves a histogram of each variable to png ﬁles, 
# outputs a scatter plot of each pair of variables to png files

# importing libraries

import pandas as pd                   # for data analysis and manupulation
from tabulate import tabulate         # for creating a table
import numpy as np                    # for plotting
import seaborn as sns                 # for plotting
import matplotlib.pyplot as plt       # for plotting
import os                             # for viewing files


# importing the iris data set
try:
    # assigning names to the columns
    raw_data = pd.read_csv("iris.data.txt", header=None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
except FileNotFoundError:
    # in case text file with the data set is not found
    print("Iris.data.txt is not found. Please download it from https://archive.ics.uci.edu/ml/datasets/iris")

# splitting iris species from the raw_data 
# adapted from https://www.kaggle.com/willvegapunk/iris-data-set
species = raw_data.Species

setosa = raw_data[species =="Iris-setosa"]
setosa.name = "Iris Setosa" # adding a name attribute 

vesticolor = raw_data[species =="Iris-versicolor"]
vesticolor.name = "Iris Vesticolor"

virginica = raw_data[species =="Iris-virginica"]
virginica.name = "Iris Virginica"

# PART 1
# defining a function that ouputs a summary for each species to a single text ﬁle
def summ(species):

    # Computations and their description taken from https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html 
    count = species.count()                     # Computing count of group
    mean = species.mean()                       # Computing mean of groups
    median = species.median()                   # Computing median of groups
    std = species.std()                         # Computing standard deviation of groups
    mad = species.mad()                         # Returning the mean absolute deviation of the values
    var = species.var()                         # Computing variance of groups
    max = species.max(numeric_only=True)        # Computing max of group values, leaving out the name of iris species
    min = species.min(numeric_only=True)        # Computing min of group values, leaving out the name of iris species

    # defining table content from the data set and the values of above computations
    TABLE_DATA = {"Summary":
        [["Count", *count],                 
        ["Mean", *mean],                   
        ["Median", *median],               
        ["Standard Deviation", *std],      
        ["Mean Absolute Deviation", *mad], 
        ["Variance", *var],                
        ["Max", *max],    
        ["Min", *min]
    ]}

    # defining future column names
    column_names = ["Statistics", "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

    # using pandas DataFrame to convert to numpy array by values with tolist
    # adapted from https://stackoverflow.com/questions/35491274/pandas-split-column-of-lists-into-multiple-columns
    TABLE_DATA2 = pd.DataFrame(TABLE_DATA)
    TABLE_DATA2[column_names] = pd.DataFrame(TABLE_DATA2.Summary.values.tolist(), index=TABLE_DATA2.index)
    TABLE_DATA3 = pd.DataFrame(TABLE_DATA2["Summary"].values.tolist(), columns= column_names)

    # deleting the last column as it only has count value
    # adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop
    TABLE_DATA3 = TABLE_DATA3.drop("Species", axis=1)

    # opening the file in append mode
    with open("Summary.txt", "a") as f:
        f.write("\n\n")
        # assigning a title to each table
        f.write(species.name)
        f.write("\n")
        # writing the information into the file in table format
        # information on tabulates was used from https://pypi.org/project/tabulate/
        f.write(tabulate(TABLE_DATA3, tablefmt="psql", headers = "keys", showindex=False))





# creating a menu for the program
# adapted from Topic 6 on functions (GMIT)
# https://github.com/olgarozhdestvina/pands-problems-2020/tree/master/Labs/Topic06-functions

def menu():
    print("\nWelcome to the Fisher's Iris Data Set!\n")
    print("Please choose one of the following:\n")
    print("\t (a) To view a summary of each Iris Species in a text file.")
    print("\t (b) To view a histogram of each Iris Species")
    print("\t (c) To view a scatter plot of each pair of variables")
    print("\t (q) To quit")
    choice = input("\nType one letter (a/b/c/q): ").strip()
    return choice

# defining function for choice (a)
def viewTextFile():
    # opening the file in write mode
    with open("Summary.txt", "w"):
        # calling the summary function
        summ(setosa) 
        summ(vesticolor)
        summ(virginica)
        # opening the file in notepad  
        file = "notepad.exe Summary.txt"
        os.system(file)
    
def viewHisogram():
    print("due")

def viewScatterPlot():
    print("due")

choicemap = {
    "a": viewTextFile,
    "b": viewHisogram,
    "c": viewScatterPlot,
    "q": quit
} 

choice = menu()
while choice != "q":
    if choice in choicemap:
        choicemap[choice] ()
    else: 
        print("\n\n Please select either a, b, c, q!")
    choice = menu()