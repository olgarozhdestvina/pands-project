# Olga Rozhdestvina
# This program  is a part of the project on Fisher's Iris Data Set
# It outputs a summary of each variable to a single text ﬁle,
# saves a histogram of each variable to png ﬁles, 
# outputs a scatter plot of each pair of variables to png files

# importing libraries

import pandas as pd                   # for data analysis and manupulation
from tabulate import tabulate         # for creating a table in the summary
import seaborn as sns                 # for plotting
import matplotlib.pyplot as plt       # for plotting
import os                             # for viewing files
import matplotlib.lines as mlines     # for a legend in scatterplot

# importing the iris data set
try:
    # assigning names to the columns
    raw_data = pd.read_csv("iris.data.txt", header=None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
except FileNotFoundError:
    # in case text file with the data set is not found
    print("Iris.data.txt is not found. Please download it from https://archive.ics.uci.edu/ml/datasets/iris")
# in case of any other error
except Exception as e:
    print("ERROR: ", e)

# splitting iris species from the raw_data 
# adapted from https://www.kaggle.com/willvegapunk/iris-data-set
species = raw_data.Species

setosa = raw_data[species =="Iris-setosa"]
setosa.name = "Iris Setosa" # adding a name attribute 

versicolor = raw_data[species =="Iris-versicolor"]
versicolor.name = "Iris Versicolor"

virginica = raw_data[species =="Iris-virginica"]
virginica.name = "Iris Virginica"



# PART 1
# defining a function that ouputs a summary for each species to a single text ﬁle

def irisSumm(species):

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
    [   
        ["Count", *count],                 
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



# PART 2
# defining a function that saves a histogram of each variable to png ﬁles

def irisHistogram(setosa, versicolor, virginica, stat):
    # setting seaborn aesthetic parametes, information used from https://seaborn.pydata.org/tutorial/aesthetics.html
    sns.set(palette="dark", style="darkgrid", context="paper", font_scale=1.25)
    # defining a size of the figure
    plt.subplots(figsize=(12,7))
    # assigning a title and ylabel
    plt.title("Iris data set comparison of {}".format(stat), fontweight="bold", fontsize=15, color="navy")
    plt.ylabel("Frequency")
    # using seaborn distplot for histogram projection
    # adopted from https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
    sns.distplot(setosa[stat], label="Iris Setosa")
    sns.distplot(versicolor[stat], label="Iris Versicolor")
    sns.distplot(virginica[stat], label="Iris Virginia")
    # changing the font size of the legend and displaying it
    plt.legend(title="Species")

    # saving a histogram as a png file into a folder
    # adapted from https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
    my_path = os.path.dirname(__file__) 
    # giving a path for saving a file
    my_folder = os.path.join(my_path, "Iris Histograms/")
    # If the directory does not exist, create it
    if not os.path.isdir(my_folder):
        os.makedirs(my_folder)
    # assigning a name to a file
    my_file = "{}.png".format(stat)
    # saving a figure 
    plt.savefig(my_folder + my_file)     
    # showing the histogram
    plt.show()



# PART 3
# defining a function that outputs a scatter plot of each pair of variables to png files

def irisScatterPlot(setosa, versicolor, virginica, stat1, stat2):
    # segregating data for future plot labels and vectors
    x = setosa[stat1]
    y = setosa[stat2]
    x2 = versicolor[stat1]
    y2 = versicolor[stat2]
    x3 = virginica[stat1]
    y3 = virginica[stat2]

    # setting seaborn aesthetic parametes 
    sns.set(palette="dark", style="darkgrid", context="paper", font_scale=1.25)

    # defining a size of the figure
    plt.subplots(figsize=(13,8))

    # drawing a scatter plot for each species
    # adopted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    # customising a palette for each plot
    cmap = sns.cubehelix_palette(dark=.2, light=.9, as_cmap=True)
    sns.scatterplot(x, y, hue=x, size=y, sizes=(30, 500), hue_norm=(0,11), style=species, palette=cmap)
    
    cmap = sns.cubehelix_palette(start=2.8, rot=-.4, as_cmap=True)
    sns.scatterplot(x2, y2, hue=x2, size=y2, sizes=(30, 500), hue_norm=(0,11), style=species, palette=cmap)
    
    cmap = sns.cubehelix_palette(rot=-.1, dark=.2, light=.9, as_cmap=True)  
    sns.scatterplot(x3, y3, hue=x3, size=y3, sizes=(30, 500), hue_norm=(0,11), style=species, palette=cmap)
    
    # assigning a title
    plt.title(stat1 + " Vs " + stat2, fontweight="bold", fontsize=15, color="DarkSlateGray")
    # drawing future handles for the legend
    # information used from https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D
    s = mlines.Line2D([],[], color="PaleVioletRed", label="Setosa", linestyle="", markeredgecolor="white", marker="o", markersize=10)
    ver = mlines.Line2D([],[], color="SeaGreen", label="Versicolor", linestyle="", markeredgecolor="white", marker="X", markersize=10)
    vir = mlines.Line2D([],[], color="SteelBlue", label="Virginica", linestyle="", markeredgecolor="white", marker="s", markersize=10)
    # overwriting the legend to remove size labels 
    # adapted from https://matplotlib.org/tutorials/intermediate/legend_guide.html 
    plt.legend(title="Species", handles=[s, ver, vir], fontsize=12, loc="upper left", fancybox=True, shadow=True)

    # saving a scatter plot as a png file into a folder
    my_path = os.path.dirname(__file__) 
    # giving a path for saving a file
    my_folder = os.path.join(my_path, "Iris Scatter Plots/")
    # If the directory does not exist, create it
    if not os.path.isdir(my_folder):
        os.makedirs(my_folder)
    # assigning a name to a file
    my_file = "{} vs {}.png".format(stat1, stat2)
    # saving a figure 
    plt.savefig(my_folder + my_file) 
    # showing the scatter plot
    plt.show()

# PART 4
# creating a menu for the program
# adapted from Topic 6 on functions (GMIT)
# https://github.com/olgarozhdestvina/pands-problems-2020/tree/master/Labs/Topic06-functions

def menu():
    print("\n Welcome to the Fisher's Iris Data Set!\n")
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
        irisSumm(setosa) 
        irisSumm(versicolor)
        irisSumm(virginica)
        # opening the file in the notepad  
        file = "notepad.exe Summary.txt"
        os.system(file)

# defining function for choice (b)    
def viewHistogram():
    # calling the histogram function
    irisHistogram(setosa, versicolor, virginica, "Sepal Length")
    irisHistogram(setosa, versicolor, virginica, "Sepal Width")
    irisHistogram(setosa, versicolor, virginica, "Petal Length")
    irisHistogram(setosa, versicolor, virginica, "Petal Width")

# defining function for choice (c)
def viewScatterPlot():
    # calling the scatter plot function
    irisScatterPlot(setosa, versicolor, virginica, "Sepal Length", "Sepal Width")
    irisScatterPlot(setosa, versicolor, virginica, "Petal Length", "Petal Width")
    irisScatterPlot(setosa, versicolor, virginica, "Sepal Length", "Petal Length")
    irisScatterPlot(setosa, versicolor, virginica, "Sepal Length", "Petal Width")
    irisScatterPlot(setosa, versicolor, virginica, "Sepal Width", "Petal Length")
    irisScatterPlot(setosa, versicolor, virginica, "Sepal Width", "Petal Width")

# setting a choicemap of 4 choices and connecting each to the correct function
choicemap = {
    "a": viewTextFile,
    "b": viewHistogram,
    "c": viewScatterPlot,
    "q": quit
} 

# requesting an input from a user
choice = menu()
while choice != "q":
    # if the choice is (a), (b) or (c)
    if choice in choicemap:
        # run the related function 
        choicemap[choice] ()
    else: # if a wrong letter is chosen
        print("\n\n Please select either a, b, c, q!")
    # return to the choice input
    choice = input("\nType one letter (a/b/c/q): ").strip()