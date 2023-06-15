from os import system
system("clear")

import csv
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r', encoding="ISO-8859-1") as csvfile:
        data = csv.reader(csvfile)
        next(csvfile)  #exclude column header
        return list(data)

class PlayerData:
    def __init__(self, P, C, A6, G6, A10, G10, A14, G14):
        self.Player = str(P)
        self.Country = str(C)
        self.Appearances_2006 = int(A6)
        self.Goals_2006 = int(G6)
        self.Appearances_2010 = int(A10)
        self.Goals_2010 = int(G10)
        self.Appearances_2014 = int(A14)
        self.Goals_2014 = int(G14)

    def goal_per_appearance(self):
        goals = self.Goals_2006 + self.Goals_2010 + self.Goals_2014
        appearances = self.Appearances_2006 + self.Appearances_2010 + self.Appearances_2014
        return round(goals / appearances, 2)

#import data
club_data = read_data('Dataset_Club Games.csv')
intl_data = read_data('Dataset_Intl Games.csv')

#create player object for club data
club_players = []
for item in club_data:
    club_players.append(PlayerData(*item))

#create player object for international data
intl_players = []
for item in intl_data:
    intl_players.append(PlayerData(*item))

#calculate goal per appearance (lambda) for each player
club_lambda = [player.goal_per_appearance() for player in club_players]
intl_lambda = [player.goal_per_appearance() for player in intl_players]

#print lambda
print(club_lambda)
print(intl_lambda)

#calculate z-scores
zscores = [round(max(l1, l2) / np.sqrt(min(l1, l2)), 2) for l1, l2 in zip(club_lambda, intl_lambda)]

#print z-scores
print(zscores)

#make a scatter plot
sc = plt.scatter(intl_lambda, club_lambda, c=zscores, cmap="viridis")
xvals = np.linspace(0, 1, num=1000)
plt.plot(xvals, xvals, linestyle="--", color="k")
plt.xlabel(r"International $\lambda$")
plt.ylabel(r"Club $\lambda$")
cb = plt.colorbar(sc)
cb.set_label("z-score")
plt.show()