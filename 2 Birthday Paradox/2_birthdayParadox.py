"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for the simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001,1,1)
        
        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
    

def getMatch(birthdays):
    """Returns the date objects of a birthday that occurs more than once
    in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # All the birthdays are unique, so retun None.
    
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA   # Retun the matching birthday
            
            
# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
      
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
Months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print ('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <=100):
        numBDays = int(response)
        break   # User has entered a valid number
print()

# Generate and display the birthdays
print('Here are', numBDays, 'birthdays: ')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        # Display a comma for each birthday after the first birthday
        print(',', end='')
    monthName = Months[birthday.month -1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if the there are two birthdays that match
match = getMatch(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    monthName = Months[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on ', dateText)
else:
    print('there are no matching birthdays')
print()
# Run through 1000 simulations
sim = int(input('Number of simulations to run? (Multiples of 10)  >> '))
print('Generating', numBDays, 'random birthdays {} times'.format(sim))
input('Press Enter to begin ...')

print('Let\'s run another {} simulations'.format(sim))
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(sim):
    # Report on the progress every sim/10 simulations
    if i % (sim/10) == 0:
        print(i, 'simulation run ...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch +1
print('{} simulation run.'.format(sim))

# Display simulation results
probability = round(simMatch / sim * 100, 2)
print('Out of {} simulations of'.format(sim), numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!!!')






