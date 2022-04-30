import pandas as pd
import numpy as np
import csv
import random

class Player:
    def __init__(self, name, points = 0):
        self.name = name
        print(f'Welcome {name}!')
        self.points = points
        print(f'Your points are: {points}')

filename = open('country-capitals.csv','r')
reader = csv.reader(filename)
country_capitals = {}
for row in reader:
    country_capitals[row[0]] = {row[1]}

player1 = input("Enter your name: ")
player1 = Player(player1)

print('Welcome to the Quiz!')
start_game = input('Start Game? Y/N: ')

if start_game != 'Y':
    print('Game Over!')
    quit()

Points = 0
Questions_Left = 10

while Questions_Left > 0:

    country = random.choice(list(country_capitals.keys()))
    capital = country_capitals.get(country)
    print(capital)
    correct_answer = capital.pop()

    print(f'What is the Capital of {country}?')
    answer = input('Answer: ')
    Questions_Left = Questions_Left - 1
    if answer == correct_answer:
        print('Correct!')
        Points = Points + 1
    else:
        print('Worng Answer!')
        print(f'The correct answer is {correct_answer}.')

print('Game Over!')
print(f'You scored {Points} Points.')
