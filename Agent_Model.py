import random
import operator
import matplotlib.pyplot
import agentframework
import time
import csv
import sys

# Start timer
start_time = time.process_time()

# Set seed (Optional)
'''
seed = 1
random.seed(seed)
'''
# Set number of agents and interations
num_of_agents = 10
num_of_iterations = 100
agents = []


# Open CSV and read in as lists
f = open("in.txt", newline = '')
reader = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
agents = []

for row in reader:
    rowlist = []
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)
#print(environment)
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
f.close()

# Create distance function
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
# Check the agents (before).
print("Before Eating and Moving")
for i in range(num_of_agents):
    print(agents[i])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# Check the agents (after).
print("After Eating and Moving")
for i in range(num_of_agents):
    print(agents[i])
    
# Plot the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

# Calculate distance between agents
maxdistance = 0; 
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
print("Distance =", distance)
maxdistance = max(maxdistance, distance)
print("Max Distance", maxdistance)

'''
with open("environment.txt", "w"):
   print(environment, sep='', end='\n', file=sys.stdout, flush=False)
f.close()
'''

# End timer
end_time = time.process_time()
print ("Elapsed run time = " + str(end_time - start_time))

