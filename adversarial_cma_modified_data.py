import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Number of users in a cell
N=[5,10,20,100];

#Total number of time slots for which the expreiment is being run
T=10000;

#List containing the average AoI for T=10000 and various values of the number of users as given in the previous list
avg_aoi=[7.4730516,12.223453,22.066736,102.02248026];


plt.xlabel("NUmber of users in a cell(N)",color="blue");
plt.ylabel("Time-averaged Average AoI(in slots)",color='blue');
plt.grid(True,alpha=0.8);
plt.title("Average AoI cost per user for T=1000",color="magenta");
plt.plot(N,avg_aoi,marker='o',markerfacecolor='yellow',color='red');
plt.show();