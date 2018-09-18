# Project 2

In this project, you'll learn about creating and calling functions, arguments, return values and math module. To start, download these two files:

* [main.py](./main.py)
* [test.py](./test.py)
* [area.csv](./area.csv)
* [population.csv](./population.csv)

You will change main.py and hand it in. You should not change test.py, and you should not hand it in; it's only purpose is to tell you your grade in advance.

After you've downloaded both files to the same directory, open your terminal, navigate to that directory, and run the following:

```
python test.py
```

You should see the following output:

```
output
```

##  Introduction
We provide you with a data file containing information about 50 states in the United States. Our task for this assignment is to look at the table and try to answer the questions that follow. We are going to write a few functions in order to make these calculations.

The table below shows a **sample** from the dataset that we have. 

<center>

| State | Area (mi²) | Population (2000) | Population (2010) | population (2014) |
|------|------|------|------|------|
|Wisconsin|65496.38 |5363675|5686986|5759432|
|Minnesota|86935.83 |44919479|5303925|5457125|
|Illinois|57913.55 |12419293|12830632|12882189|

</center>

1. What is the value of the maximum land area among any three given states?
2. What is the least value of population density among the states of Iowa, Kansas and Michigan?
3. For a given state, what’s the predicted population in the given year? (The function will take in values of initial year, final year, growth rate and state name)
4. Between any two given years, what is the population growth rate of particular state?

Please make sure the data file area.csv and population.csv are in the same folder with main.py. We don’t require you to know how to read from data file so we provides the following function.

### Provided Function in Module project.py
**getArea(stateName)** 

getArea function takes the name of one state as an argument and returns the size of this state area.

```
>>> import project
>>> project.getArea("Wisconsin")
>>> 65498
```
**getPopulation(stateName, year)**

getPopulation function takes the name of one state and a year as arguments and returns the population of this state in this year.

```
>>> import project
>>> project.getPopulation("Wisconsin", 1990)
>>> 490500
```

## Program Requirements
You will write **at least four(4)** functions with the following names and behaviors:

**getMaximumLand(stateName1, stateName2, stateName3)**

Find the max value for land area among the three given area values which will be passed as parameters. To do this we can use the inbuilt [max()](https://docs.python.org/2/library/functions.html#max) function.

Example:

```
>>> getMaximumLand("Wisconsin", "Iowa", "Minnesota")
```

**getMinimumPopulationDensity(stateName1, stateName2, stateName3, year)**

Population density is measured as population per unit area. The formula to calculate population density is:
**Population Density = Population / Land Area**. For this function, you need to retrieve population and area values for the given states and calculate the density. We then find the min value of population density among the three values passed as parameters. To do this, we can use the inbuilt [min()](https://docs.python.org/2/library/functions.html#min) function.

Example:

```
>>> getMinimumPopulationDensity("Wisconsin", "Iowa", "Minnesota", 2000)
```

**calcNewPopulation(stateName, growthRate, yearA, yearB)**

We use the following formula for population growth prediction in this question: <img src="Population.png" alt="drawing" width="100"/>. Here,

 1. <img src="Pa.png" alt="drawing" width="15"/> is the population for the specific state in year *a*.
 2. <img src="Pb.png" alt="drawing" width="15"/> is the predicted population for the specific state in year *b*, *b* > *a*. 
 3. *r* is the growth rate.
 4. *t* is the number of years between year *a* and the year *b*.

To implement this function, You can use exp function in Python [math library](https://docs.python.org/3/library/math.html).
The function should take in the values for the state name, state growth rate and year *a* and year *b*. It should return the value of the predicted population in year *b*. 

Example:

```
>>> calcNewPopulation("Wisconsin", 0.5, 2000, 2010)
>>> 
```

**calcGrowthRate(stateName, yearA, yearB)**

Use the same formula as above to calculate the rate of growth. To do this, you can use the log fucntion present in Python [math library](https://docs.python.org/3/library/math.html). 

Example:

```
>>> calcGrowthRate("Wisconsin", 2000, 2010)
```

**Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.**
