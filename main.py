from project import *


# Insert getMaximumLand(stateName1, stateName2, stateName3) function here
# Step1: Retrieve area values for all 3 states using getArea function and assign it to variables.
# Step2: Use max() function to calculate the max value and store it as a variable
# Step3: Return the max value that you calculated.


# Insert getMinimumPopulationDensity(stateName1, stateName2, stateName3, year) function here
# Step1: Retrieve area and population values for all 3 states using getArea and the getPopulation function and assign it to variables.
# Step2: Use min() function to calculate the max value and store it as a variable
# Step3: Return the min value that you calculated.


# Insert calcNewPopulation(stateName, growthRate, yearA, yearB): function here
# Step 1: Using the statename retrieve the intial population for yearA
# Step 2: Calculate time between yearA and yearB
# Step 3: Use the math.exp() function in the given formula to calculate final population
# Step 4: Return the final population

# Insert calcGrowthRate(stateName, finalPopulation, initPopulation, year1, year2) function here
# Step 1: Using the statename retrieve the intial population for yearA
# Step 1: Using the statename retrieve the final population for yearB
# Step 2: Calculate time between yearA and yearB
# Step 3: Use the math.log() function in the given formula to calculate growth rate
# Step 4: Return the final population


if __name__ == "__main__":
    #Example state names. Please play around by changing the state names
    state1Name = "Wisconsin"
    state2Name = "Iowa"
    state3Name = "Minnesota"

    # Solving Q1: Finding max Area
    # Here we call the function and see if it gives the correct output
    # Play around by changing the state names and your program should still work.
    maxArea = getMaximumLand (state1Name, state2Name, state3Name)
    print ("The maximum land area among the three states %s, %s and %s : " % (state1Name, state2Name, state3Name))
    print (maxArea)

    # Solving Q2: Finding minimum Population Density
    # Play around by changing the state names and the year and your program should still work.
    minPopulationDensity = getMinimumPopulationDensity(state1Name, state2Name, state3Name,2000)
    print ("The minimum population density among the three states %s, %s and %s : " % (state1Name, state2Name, state3Name))
    print (minPopulationDensity)

    # Solving Q3: Finding final population
    # Play around by changing the state names and the year and your program should still work.
    newPopulation = calcNewPopulation(state1Name, 0.5, 2000,2010)
    print ("The new population for %s : " % state1Name)
    print (newPopulation)

    # Solving Q4: Finding minimum Population Density
    # Play around by changing the state names and the year and your program should still work.
    growthRate = calcGrowthRate(state1Name, 2000, 2010)
    print ("The growth rate  for %s : " % state1Name)
    print (growthRate)



