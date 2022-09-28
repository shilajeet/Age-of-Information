import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#The energy arrivals are Poisson process with interarrival times being i.i.d exponentially distributed with parameter \lambda=1
time=[];
time.append(0);
while max(time)<=500:
     time.append(time[-1]+np.random.exponential(1));

#length of time horizon
T=500;

#variable to store age
age=0;

#The energy arrives by a poisson process
energy=[];
energy.append(1);
for i in range(1,len(time)):
     energy.append(np.random.exponential(1));

#variable to store sum energy
sum_en=0;

#list storing the Poisson energy arrivals (A_i 's)
energy_A=[];
     
#list to store the time at which the receiver can make an update
time_len=[];

for i in range(0,len(time)):
     
     if sum_en<1:
          sum_en=sum_en + energy[i];
          if sum_en>=1:
               energy_A.append(sum_en);
               sum_en=0;
               time_len.append(time[i]);
# =============================================================================
#      elif sum_en>=1:
#           energy_A.append(sum_en);
#           sum_en=0;
#           time_len.append(time[i]);
# =============================================================================
          
#Probability of update being erased (1-p)
p=0.6;

#time of status updates at the receiver
rx_ux=[];

#for iterate in range(0,Monte_Carlo):
Monte_Carlo=1000;

for i in range(0,len(time_len)):
          
          toss=np.random.binomial(1,p);
          
          if toss==1:
               rx_ux.append(time_len[i]);
     
for i in range(0,len(rx_ux)-1):
     age=age+(np.square(rx_ux[i+1]-rx_ux[i]))/2;
     
age=age+(np.square(T-max(rx_ux)))/2;  
     