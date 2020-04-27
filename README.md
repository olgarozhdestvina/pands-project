# Programming and Scripting Project

This document contains the Project 2020 for Programming and Scripting Module at GMIT. 

*Submitted by:* Olga Rozhdestvina (Student No: G00387844) 

*Lecturers:* Ian McLoughlin, Andrew Beatty 

*Programming Language used:* [Python](https://www.python.org/)

------

## Table of Contents

* [Fisher's Iris Data Set](https://github.com/olgarozhdestvina/pands-project#fisher's-iris-data-set)
* [About the Data Set](https://github.com/olgarozhdestvina/pands-project#about-the-data-set)
* [Use of the Set](https://github.com/olgarozhdestvina/pands-project#use-of-the-set)
* [Set up](https://github.com/olgarozhdestvina/pands-project#set-up)
* [How to run the code](https://github.com/olgarozhdestvina/pands-project#how-to-run-the-code)
* [Analysing the Set](https://github.com/olgarozhdestvina/pands-project#analysing-the-set)
* [License](https://github.com/olgarozhdestvina/pands-project#license)
* [Acknowledgment](https://github.com/olgarozhdestvina/pands-project#acknowledgment)


### Fisher's Iris Data Set

##### About the Data Set

*The Iris flower data set* or *Fisher’s Iris data set* was presented in 1936 as an example for linear discriminant analysis in the work of British statistician and geneticist Sir Ronald Aylmer Fisher, titled __*“The use of multiple measurements in taxonomic problems”*__. However, sometimes it is called *Anderson's Iris data set*  as the data itself originated in research by Edgar Anderson, who studied morphologic variations in Iris flowers of three related species: 

·   Iris setosa

·   Iris versicolor 

·   Iris virginica. 

  ![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Used%20Images/iris-species.jpg)

 The data set presents 150 samples of flowers (50 for each plant), featuring four attributes (data **features**):

·   Sepal length

·   Sepal width

·   Petal length

·   Petal width,

all four measured in centimetres. Additionally, the species was recorded for each plant. The combination of these four features served as a base for Fisher’s linear discriminant model for distinguishing the species from each other. 

 

##### Use of the Set

The Iris flower data set is famous among pattern recognition scientists and statisticians, and has been referenced to illustrate a variety of techniques, for instance, in machine learning, multivariate statistics, data mining, pattern recognition etc. Moreover, it is frequently offered as a standard example data set in various software and other sources, and so has an important contribution not only to science, but also to teaching machine learning. 

------



### Set up

The raw data was taken from  [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris). 

Programs used for completion of this project are: [Visual Studio Code](https://code.visualstudio.com/), [cmder](http://cmder.net/)

Libraries used for the project are: [tabulate](https://pypi.org/project/tabulate/), [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [matplotlib.lines](https://matplotlib.org/api/lines_api.html), [seaborn](https://seaborn.pydata.org/) and [os](https://docs.python.org/3/library/os.html). All of these are installed with the [Anaconda Python distribution](https://www.anaconda.com/). 

 

###  How to run the code

1. Make sure that you have Python installed
2. Download or clone the current repository "pands-project"
3. Open Command Interpreter 
4. Get into correct directory
5. Run python code by typing *python analysis.py*

------

### Analysing the Set

The purpose of the program analysis.py is to complete three tasks on anasysing the Iris Data Set: 

1. to output a summary of each Iris species to a single text ﬁle;
2. to save a histogram of each variable to png ﬁles;
3. to save a scatter plot of each pair of variables to png files.

The program has a multiple choice menu which allows selecting between viewing the text file with the summary, viewing the histograms or viewing the scatter plots. Please note that all files will be automatically saved to your PC.

 ![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Used%20Images/menu.jpg)


The Iris data set is stored in .txt format (refer to https://github.com/olgarozhdestvina/pands-project/blob/master/iris.data.txt) In this programme, it is first loaded into Pandas DataFrame and then split per Iris species.


The choice _a_ in the menu is to view the summary, which includes the following descriptive statistics: Count, Mean, Median, Standard Deviation, Mean Absolute Deviation, Variance, as well as Maximum and Minimum for the four data features in each species. The result of these computations is below:

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Used%20Images/Iris_Summary.jpg)

Computing the Count of the different species present confirmed that the data set is balanced as there is an equal distribution of classes within the data set (50 rows for each species)

Calculating the Mean and the Median for measuring the data's **central tendency** indicates that the values are distributed symmetrically  with low presence of outliers.

The **variation** of the data is determined by computing Variance, Standard Deviation and Mean Absolute Deviation. Low values of all three statistics  in each species imply that the Mean is indicative of other values in the data set and that the data is relatively concentrated (which makes it reliable without addititonal samples).

From analysis of Maximum and Minimum values Virginica appears to be the largest species (by 3 out of 4 features) and Setosa the smallest (by 3 out of 4 features as well). Versicolor is the medium by all 4 parameteres. 


The choice _b_ in the menu outputs histograms on how each feature is distributed with respect to the frequency. 

The histograms of Sepal Length and Sepal Width depict a significant overlapping in distribution. 

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Histograms/Sepal%20Length.png)
![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Histograms/Sepal%20Width.png)

In contrast, the histograms of Petal Length and Petal Width show that the Setosa Petal's distribution is quite different. The least overlapping in all three species is seen in the histogrm with Petal Width; therefore it can be used as a distinguishing factor in terms of the distribution of the species.

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Histograms/Petal%20Length.png) ![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Histograms/Petal%20Width.png)


The choice _c_ creates scatter plots for each pair of features.

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Sepal%20Length%20vs%20Sepal%20Width.png)

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Sepal%20Length%20vs%20Petal%20Length.png)

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Sepal%20Length%20vs%20Pepal%20Width.png)

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Sepal%20Width%20vs%20Petal%20Width.png)

![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Sepal%20Width%20vs%20Petal%20Length.png)
![](https://raw.githubusercontent.com/olgarozhdestvina/pands-project/master/Iris%20Scatter%20Plots/Petal%20Length%20vs%20Petal%20Width.png)

Analysis of all six scatter plots shows a distinct separation of Setosa from Versicolor and Virginica. It also confirms the previous statement that Setosa is the smallest of the three species (except for Sepal Width). The least overlapping in Versicolor and Virginica is depicted in the Petal Length Vs Petal Width plot.


The choice _q_ in the menu is for exiting the program.


------

#### License

This project is licensed under the MIT License - see the LICENSE.md file for details



#### Acknowledgment

- Lecturers of GMIT for this module: Ian McLoughlin and Andrew Beatty 
- https://stackoverflow.com/
- https://jakevdp.github.io/WhirlwindTourOfPython/
- https://www.datacamp.com/
- https://realpython.com/
- https://github.com/
- https://www.kaggle.com
- https://archive.ics.uci.edu
- https://pandas.pydata.org
- https://pypi.org
- https://seaborn.pydata.org
- https://matplotlib.org
- https://www-users.cs.umn.edu/~kumar001/dmbook/data_exploration_1st_edition.pdf
