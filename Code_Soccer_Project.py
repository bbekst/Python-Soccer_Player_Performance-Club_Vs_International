#import libraries
import csv
import matplotlib.pyplot as plt

#define function to import data
def read_data(filename):
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile)
        next(csvfile)  #exclude column header
        return list(data)

#define function to calculate goal per appearance
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

    def GPA(self):
        goals = self.Goals_2006 + self.Goals_2010 + self.Goals_2014
        appearances = self.Appearances_2006 + self.Appearances_2010 + self.Appearances_2014
        return round(goals / appearances, 2)

#import data
club_data = read_data('Dataset_Club Games.csv')
intl_data = read_data('Dataset_Intl Games.csv')

#create player object for club data
club_players = []
for i in club_data:
    club_players.append(PlayerData(*i))

#create player object for international data
intl_players = []
for i in intl_data:
    intl_players.append(PlayerData(*i))

#calculate goal per appearance (GPA)
club_GPA = [player.GPA() for player in club_players]
intl_GPA = [player.GPA() for player in intl_players]

#print GPA
print(club_GPA)
print(intl_GPA)

#calculate absolute differences
diffs = []
for club, intl in zip(club_GPA, intl_GPA):
    diffs.append(round(abs(club - intl), 2))

#print results
print(diffs)

#make a scatter plot
sc = plt.scatter(intl_GPA, club_GPA, c=diffs)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlabel(r"Intl GPA")
plt.ylabel(r"Club GPA")
plt.colorbar(sc).set_label('Differences')
plt.show()