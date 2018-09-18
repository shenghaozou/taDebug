# Project 2

In this project, you'll learn about creating and calling functions, arguments, return values and math module. To start, download these two files:

* [main.py]()
* [test.py]()
* [area.csv]()
* [population.csv]()

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
We provide you with a data file containing information about 51 states in the United States. Our task for this assignment is to look at the table and try to answer the questions that follow. We are going to write a few functions in order to make these calculations.

The table below shows the population and land area for 3 neighboring states. (In our dataset we have 51 states.)

| State | Area | Population (1990) | Population (2018) |
|-------|------|------------------|------------------|
|Wisconsin|65,498 mi²|4,905,000|5,795,000|
|Minnesota|86,943 mi²|4,390,000|5,577,000|
|Illinois|57,915 mi²|11,450,000|12,770,000|

1. Given 3 states, what is the value of the maximum land area among these three?
2. Given 3 states, what is the population density value for the state with least population density for the year 2018?
3. Given a growth rate of 0.5, what will be the population in of Wisconsin in 2019?
4. Between the year 1990 and 2018, what was the population growth rate in Minnesota?

Please make sure the data file area.csv and population.csv are in the same folder with main.py. We don’t require you to know how to read from data file so we provides the following function.

### Provided Function in Module project.py:
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

1. **getMaximumLand(stateName1, stateName2, stateName3)**: Find the max value for land area among the three given area values which will be passed as parameters. To do this we can use the inbuilt [max()](https://docs.python.org/2/library/functions.html#max) function.
2. **getMinimumPopulationDensity(stateName1, stateName2, stateName3, year)**: Population density is measured as population per unit area. The formula to calculate population density is:
**Population Density = Population / Land Area**. For this function, you need to retrieve population and area values for the given states and calculate the density. We then find the min value of population density among the three values passed as parameters. To do this, we can use the inbuilt [min()](https://docs.python.org/2/library/functions.html#min) function.
3. **calcNewPopulation(initPopulation, growthRate, time)**: We use the following formula for population growth prediction in this question: <img src="population.png" alt="drawing" width="100"/>. Here,
    1. <img src="Pa.png" alt="drawing" width="15"/> is the population for the specific state in year *a* (the initial population).
    2. <img src="Pb.png" alt="drawing" width="15"/>is the population for the specific state in year *b* (the final population), *b* > *a*. 
    3. *r* is the growth rate.
    4. *t* is the number of years between year *a* and the year *b*.
4. **calcGrowthRate(stateName, finalPopulation, initPopulation, year1, year2)**: Use the same formula as above to calculate the rate of growth. To do this, you can use the math.log() module present in the math library. 

**Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.**