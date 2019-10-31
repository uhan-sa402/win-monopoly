import sys
import numpy as np
from numpy.matlib import zeros
np.set_printoptions(threshold=sys.maxsize)

states = list(range(40))
names = ['Go', 'Mediterranean Avenue', 'Community Chest 1',
         'Baltic Avenue', 'Income Tax', 'Reading Railroad',
         'Oriental Avenue', 'Chance 1', 'Vermont Avenue',
         'Connecticut Avenue', 'Jail',
         'St. Charles Place', 'Electric Company', 'States Avenue',
         'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place',
         'Community Chest 2', 'Tennessee Avenue', 'New York Avenue',
         'Free Parking', 'Kentucky Avenue', 'Chance 2', 'Indiana Avenue',
         'Illinois Avenue', 'B&O Railroad', 'Atlantic Avenue',
         'Ventnor Avenue', 'Water Works', 'Marvin Gardens',
         'Go to Jail', 'Pacific Avenue', 'North Carolina Avenue',
         'Community Chest 3', 'Pennsylvania Avenue', 'Short Line',
         'Chance 3', 'Park Place', 'Luxury Tax', 'Boardwalk']
name = dict(zip(states, names))
state = dict(zip(names, states))

rolls = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
probs = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
prob = dict(zip(rolls, probs))

# Initialize probability matrix
P = zeros((40, 40))

# Compute base transition probabilities
for last in states:
    for roll in rolls:

        # Find the next board position
        # If we've landed on 'Go to Jail', we go to 'Jail'
        # Otherwise, we progress forward in the usual way
        if name[last] == 'Go to Jail':
            now = state['Jail'] + roll
        else:
            now = (last + roll) % 40

        # Compute the transition probability
        P[last, now] = prob[roll]

# Adjust base probabilities for Chance and Community Chest positions
for last in states:
    for roll in rolls:

        # Find the next board position
        # If we've landed on 'Go to Jail', we go to 'Jail'
        # Otherwise, we progress forward in the usual way
        if name[last] == 'Go to Jail':
            now = state['Jail'] + roll
        else:
            now = (last + roll) % 40

        # Adjust the transition probabilities
        if name[now] == 'Chance 1':
            P[last, state['Go']]                    += (1/16) * prob[roll]    # Go
            P[last, state['Reading Railroad']]      += (1/16) * prob[roll]    # Reading Railroad
            P[last, state['St. Charles Place']]     += (1/16) * prob[roll]    # St Charles Place
            P[last, state['Illinois Avenue']]       += (1/16) * prob[roll]    # Illinois Avenue
            P[last, state['Go to Jail']]            += (1/16) * prob[roll]    # Jail
            P[last, state['Boardwalk']]             += (1/16) * prob[roll]    # Boarwalk
            P[last, state['Electric Company']]      += (1/16) * prob[roll]    # Nearest utility
            P[last, state['Pennsylvania Railroad']] += (1/16) * prob[roll]    # Nearest railroad
            P[last, now - 3]                        += (1/16) * prob[roll]    # 3 spaces back
            P[last, now]                             = (7/16) * prob[roll]    # Stay put
        elif name[now] == 'Chance 2':
            P[last, state['Go']]                    += (1/16) * prob[roll]    # Go
            P[last, state['Reading Railroad']]      += (1/16) * prob[roll]    # Reading Railroad
            P[last, state['St. Charles Place']]     += (1/16) * prob[roll]    # St Charles Place
            P[last, state['Illinois Avenue']]       += (1/16) * prob[roll]    # Illinois Avenue
            P[last, state['Go to Jail']]            += (1/16) * prob[roll]    # Jail
            P[last, state['Boardwalk']]             += (1/16) * prob[roll]    # Boarwalk
            P[last, state['Water Works']]           += (1/16) * prob[roll]    # Nearest utility
            P[last, state['B&O Railroad']]          += (1/16) * prob[roll]    # Nearest railroad
            P[last, now - 3]                        += (1/16) * prob[roll]    # 3 spaces back
            P[last, now]                             = (7/16) * prob[roll]    # Stay put
        elif name[now] == 'Chance 3':
            P[last, state['Go']]                    += (1/16) * prob[roll]    # Go
            P[last, state['Reading Railroad']]      += (1/16) * prob[roll]    # Reading Railroad
            P[last, state['St. Charles Place']]     += (1/16) * prob[roll]    # St Charles Place
            P[last, state['Illinois Avenue']]       += (1/16) * prob[roll]    # Illinois Avenue
            P[last, state['Go to Jail']]            += (1/16) * prob[roll]    # Jail
            P[last, state['Boardwalk']]             += (1/16) * prob[roll]    # Boarwalk
            P[last, state['Electric Company']]      += (1/16) * prob[roll]    # Nearest utility
            P[last, state['Reading Railroad']]      += (1/16) * prob[roll]    # Nearest railroad
            P[last, now - 3]                        += (1/16) * prob[roll]    # 3 spaces back
            P[last, now]                             = (7/16) * prob[roll]    # Stay put
        elif name[now].startswith('Community Chest'):
            P[last, state['Go']]         += (1/16) * prob[roll]    # Go
            P[last, state['Go to Jail']] += (1/16) * prob[roll]    # Jail
            P[last, now]                  = (14/16) * prob[roll]   # Stay put

rent = zeros((40, 1))
rent[state['Mediterranean Avenue']] = 2
rent[state['Baltic Avenue']] = 4
rent[state['Oriental Avenue']] = 6
rent[state['Vermont Avenue']] = 6
rent[state['Connecticut Avenue']] = 8
rent[state['St. Charles Place']] = 10
rent[state['States Avenue']] = 10
rent[state['Virginia Avenue']] = 12
rent[state['St. James Place']] = 14
rent[state['Tennessee Avenue']] = 14
rent[state['New York Avenue']] = 16
rent[state['Kentucky Avenue']] = 18
rent[state['Indiana Avenue']] = 18
rent[state['Illinois Avenue']] = 20
rent[state['Atlantic Avenue']] = 22
rent[state['Ventnor Avenue']] = 22
rent[state['Marvin Gardens']] = 24
rent[state['Pacific Avenue']] = 26
rent[state['North Carolina Avenue']] = 26
rent[state['Pennsylvania Avenue']] = 28
rent[state['Park Place']] = 35
rent[state['Boardwalk']] = 50
