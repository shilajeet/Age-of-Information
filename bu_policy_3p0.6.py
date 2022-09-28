import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Number of Monte Carlo Simulations
Monte_Carlo=1000;

slots=[20,30,40,50,60,70,80,90,100,200,300,500,1000,1500,2000,2500,3000];

#Probability of update being erased (1-p)
p=0.6;

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
          sum_en=0;
          
          energy_A=[];
          
          #Array to store scheduled status updates time
          time_len=[];
          
          #Array to store actual updates time
          time_s1=[];
          
          for i in range(0,len(time)):
               sum_en=sum_en+np.random.exponential(1);
               energy.append(sum_en);
               
               if sum_en>=1:
                    energy_A.append(sum_en);
                    sum_en=0;
                    time_len.append(time[i]);
          
          samp_sum=0;
          
          for i in range(0,len(time)):
               samp_sum=samp_sum+energy[i];
               if samp_sum>=1:
                    samp_sum=samp_sum-1;
                    toss=np.random.binomial(1,p);
                    if toss==1:
                        time_s1.append(time[i]); 
                         
          #variable to store age
          age=0;

          for i in range(0,len(time_s1)-1):
               age=age+(np.square(time_s1[i+1]-time_s1[i]))/2;
               
          age=age+(np.square(slots[num]-max(time_s1)))/2;
          
          
          age_list.append(age/slots[num]);
          
     age_list2.append(np.mean(age_list));
cong=np.zeros((1,len(slots)));     
cong[:]=(2-p)/(2*p);  
cong=np.transpose(cong);   
plt.xlabel("time",color='blue');
plt.ylabel("Time Average AoI",color='blue');
plt.plot(slots,age_list2);

plt.plot(slots,cong,'g--');
plt.legend(['sample average p=0.6','lower bound p=0.6']);
plt.ylim(0,7);
plt.grid(True,alpha=0.8);
plt.show();      
     
     
     
     