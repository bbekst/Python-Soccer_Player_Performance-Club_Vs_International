import csv
with open('Dataset_Club Games.csv', 'r', encoding="ISO-8859-1") as csvfile:
    data = csv.reader(csvfile)
    next(csvfile)  #this will exclude the column header
    clubdata1 = []
    for i in data:
        clubdata1.append(i) #this will convert the object file into list

class club_data: #formatting my entries
    def __init__(self, P, C, A6, G6, A10, G10, A14, G14):
        self.Player = str(P)
        self.Country = str(C)
        self.Appearances_2006 = int(A6)
        self.Goals_2006 = int(G6)
        self.Appearances_2010 = int(A10)
        self.Goals_2010 = int(G10)
        self.Appearances_2014 = int(A14)
        self.Goals_2014 = int(G14)

    def goalperappearance (sample): #to calculate goals per appearance
        goals_club = 0
        appearances_club = 0
        for club in sample:
            goals_club += club.Goals_2006 + club.Goals_2010 + club.Goals_2014
            appearances_club += club.Appearances_2006 + club.Appearances_2010 + club.Appearances_2014
        return round(goals_club/appearances_club,2)

clubdata2 = []
for i in clubdata1:
    clubdata2.append(club_data(*i[0:]))

#now let's repeat the same for international games

with open('Dataset_Intl Games.csv', 'r', encoding="ISO-8859-1") as csvfile:
    intldata = csv.reader(csvfile)
    next(csvfile)  # this will exclude the column header
    intldata1 = []
    for i in intldata:
        intldata1.append(i) #this will convert the object file into list

class intl_data: #formatting my entries
    def __init__(self, P, C, A6, G6, A10, G10, A14, G14):
        self.Player = str(P)
        self.Country = str(C)
        self.Appearances_2006 = int(A6)
        self.Goals_2006 = int(G6)
        self.Appearances_2010 = int(A10)
        self.Goals_2010 = int(G10)
        self.Appearances_2014 = int(A14)
        self.Goals_2014 = int(G14)

    def goalperappearance (sample): #to calculate goals per appearance
        goals_intl = 0
        appearances_intl = 0
        for intl in sample:
            goals_intl += intl.Goals_2006 + intl.Goals_2010 + intl.Goals_2014
            appearances_intl += intl.Appearances_2006 + intl.Appearances_2010 + intl.Appearances_2014
        return round(goals_intl/appearances_intl,2)

intldata2 = []
for i in intldata1:
    intldata2.append(intl_data(*i[0:]))

#now, let's calculate individual player's lamda(λ):

#lambda(λ) of cristiano ronaldo (cr) for club

cr_club_data3 = []
cr_club_data3.append(clubdata2[0])
cr_club=club_data.goalperappearance(cr_club_data3)

#lambda(λ) of cristiano ronaldo (cr) for intl

cr_intl_data3 = []
cr_intl_data3.append(intldata2[0])
cr_intl=intl_data.goalperappearance(cr_intl_data3)

#lambda(λ) of lionel messi (lm) for club

lm_club_data3 = []
lm_club_data3.append(clubdata2[1])
lm_club=club_data.goalperappearance(lm_club_data3)

#lambda(λ) of lionel messi (lm) for intl

lm_intl_data3 = []
lm_intl_data3.append(intldata2[1])
lm_intl=intl_data.goalperappearance(lm_intl_data3)

#lambda(λ) of sergio ramos (sr) for club

sr_club_data3 = []
sr_club_data3.append(clubdata2[2])
sr_club=club_data.goalperappearance(sr_club_data3)

#lambda(λ) of sergio ramos (sr) for intl

sr_intl_data3 = []
sr_intl_data3.append(intldata2[2])
sr_intl=intl_data.goalperappearance(sr_intl_data3)

#lambda(λ) of rafael marquez (rm) for club

rm_club_data3 = []
rm_club_data3.append(clubdata2[3])
rm_club=club_data.goalperappearance(rm_club_data3)

#lambda(λ) of rafael marquez (rm) for intl
rm_intl_data3 = []
rm_intl_data3.append(intldata2[3])
rm_intl=intl_data.goalperappearance(rm_intl_data3)

#lambda(λ) of xavi (xa) for club

xa_club_data3 = []
xa_club_data3.append(clubdata2[4])
xa_club=club_data.goalperappearance(xa_club_data3)

#lambda(λ) of xavi (xa) for intl

xa_intl_data3 = []
xa_intl_data3.append(intldata2[4])
xa_intl=intl_data.goalperappearance(xa_intl_data3)

#lambda(λ) of andres iniesta (ai) for club

ai_club_data3 = []
ai_club_data3.append(clubdata2[5])
ai_club=club_data.goalperappearance(ai_club_data3)

#lambda(λ) of andres iniesta (ai) for intl

ai_intl_data3 = []
ai_intl_data3.append(intldata2[5])
ai_intl=intl_data.goalperappearance(ai_intl_data3)

#lambda(λ) of andres guardado (ag) for club

ag_club_data3 = []
ag_club_data3.append(clubdata2[6])
ag_club=club_data.goalperappearance(ag_club_data3)

#lambda(λ) of andres guardado (ag) for intl

ag_intl_data3 = []
ag_intl_data3.append(intldata2[6])
ag_intl=intl_data.goalperappearance(ag_intl_data3)

#lambda(λ) of wesley sneijder (ws) for club

ws_club_data3 = []
ws_club_data3.append(clubdata2[7])
ws_club=club_data.goalperappearance(ws_club_data3)

#lambda(λ) of wesley sneijder (ws) for intl

ws_intl_data3 = []
ws_intl_data3.append(intldata2[7])
ws_intl=intl_data.goalperappearance(ws_intl_data3)

#lambda(λ) of tim cahill (tc) for club

tc_club_data3 = []
tc_club_data3.append(clubdata2[8])
tc_club=club_data.goalperappearance(tc_club_data3)

#lambda(λ) of tim cahill (tc) for intl

tc_intl_data3 = []
tc_intl_data3.append(intldata2[8])
tc_intl=intl_data.goalperappearance(tc_intl_data3)

#lambda(λ) of miroslav klose (mk) for club

mk_club_data3 = []
mk_club_data3.append(clubdata2[9])
mk_club=club_data.goalperappearance(mk_club_data3)

#lambda(λ) of miroslav klose (mk) for intl

mk_intl_data3 = []
mk_intl_data3.append(intldata2[9])
mk_intl=intl_data.goalperappearance(mk_intl_data3)

#lambda(λ) of philipp lahm (pl) for club

pl_club_data3 = []
pl_club_data3.append(clubdata2[10])
pl_club=club_data.goalperappearance(pl_club_data3)

#lambda(λ) of philipp lahm (pl) for intl

pl_intl_data3 = []
pl_intl_data3.append(intldata2[10])
pl_intl=intl_data.goalperappearance(pl_intl_data3)

#lambda(λ) of bastian schweinsteiger (bs) for club

bs_club_data3 = []
bs_club_data3.append(clubdata2[11])
bs_club=club_data.goalperappearance(bs_club_data3)

#lambda(λ) of bastian schweinsteiger (bs) for intl

bs_intl_data3 = []
bs_intl_data3.append(intldata2[11])
bs_intl=intl_data.goalperappearance(bs_intl_data3)

#In order to measure variability of data, let's calculate z scores

#To evaluate, the performance difference will be considered as statistically significant if z-score is higher than 1

#Summary of lambda (λ):

intl = [[1,cr_intl],[2,lm_intl],[3,sr_intl],[4,rm_intl],[5,xa_intl],[6,ai_intl],[7,ag_intl],[8,ws_intl],[9,tc_intl],[10,mk_intl],[11,pl_intl],[12,bs_intl]]
club = [[1,cr_club],[2,lm_club],[3,sr_club],[4,rm_club],[5,xa_club],[6,ai_club],[7,ag_club],[8,ws_club],[9,tc_club],[10,mk_club],[11,pl_club],[12,bs_club]]

#where 1=cr, 2=lm, 3=sr, 4=rm, 5=xa, 6=ai, 7=ag, 8=ws, 9=tc, 10=mk, 11=pl, 12=bs just like marked while calculating lamda (λ)

#let's put data into x, y tuples

x1, y1 =zip(*intl)
x2, y2 = zip(*club)

import numpy as np

#z_scores:

zscores = []
for lambda1, lambda2 in zip(y1, y2):
    l1 = max(lambda1, lambda2)
    l2 = min(lambda1, lambda2)
    zscore = round(l1/np.sqrt(l2),2)
    zscores.append(zscore)

#now, let's plot the individual players' lambda

import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator, interp1d

#let's create the interpolator

bci1 = interp1d(x1, y1, kind="cubic")
bci2 = interp1d(x2, y2, kind="cubic")

#let's define dense x-axis for interpolating over

x1_new = np.linspace(min(x1), max(x1), 1000)
x2_new = np.linspace(min(x2), max(x2), 1000)

#Let's make a scatter plot

sc = plt.scatter(y1, y2, c=zscores, cmap="viridis")

#Let's add one-to-one line

xvals = np.linspace(0, 1, num=1000)
plt.plot(xvals, xvals, linestyle="--", color="k")
plt.xlabel(r"International $\lambda$")
plt.ylabel(r"Club $\lambda$")
cb = plt.colorbar(sc)
cb.set_label("z-score")
plt.show()

print(zscores)

# Looking at the individual calculated scores, scatter plot and our evaluation criteria, we can conclude that only 3 players out of 12 (Cristiano Ronaldo,
# Lionel Messi & Miroslav Klose) have significantly different performances (based on respective z-scores: 1.33, 1.38 & 1.27 which is >1) between club &
# international games, hence, we accept our null hypothesis and conclude that the player's performance is not different in the club and international games.
