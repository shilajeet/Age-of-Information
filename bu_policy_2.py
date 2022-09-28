import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

#for iterate in range(0,Monte_Carlo):
Monte_Carlo=1000;


slots=[100,200,300,500,1000,1500,2000,2500,3000];

#Probability of update being erased (1-p)
p=1;

age_list2=[];

for num in range(0,len(slots)):
     age_list=[]; 
     for iterate in range(0,Monte_Carlo): 
          time=[];
          time.append(0);
          
          
          while max(time)<=slots[num]:
               time.append(time[-1]+np.random.exponential(1));
               
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
                         
          #time of status updates at the receiver
          rx_ux=[];
          
          for i in range(0,len(time_len)):
               
               toss=np.random.binomial(1,p);
               if toss==1:
                    rx_ux.append(time_len[i]);
          
          #variable to store age
          age=0;         
          
          for i in range(0,len(rx_ux)-1):
               age=age+(np.square(rx_ux[i+1]-rx_ux[i]))/2;
          
          age=age+(np.square(slots[num]-max(rx_ux)))/2;
          
          age_list.append(age/slots[num]);
          
     age_list2.append(np.mean(age_list));
                             
plt.xlabel("time",color='blue');
plt.ylabel("Time Average AoI",color='blue');
plt.plot(slots,age_list2);
plt.ylim(0,7);
plt.grid(True,alpha=0.8);
plt.show();                    
          
          
     