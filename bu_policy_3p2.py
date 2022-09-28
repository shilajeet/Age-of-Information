import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Number of Monte Carlo Simulations
Monte_Carlo=100;

slots=[40,50,60,70,80,90,100,200,300,500,1000,1500,2000,2500,3000];


#Probability of update being erased (1-p)
p=0.2;

age_list2=[];

for num in range(0,len(slots)):
     age_list=[]; 
     for iterate in range(0,Monte_Carlo): 
          time=[];
          time.append(0);
          
          while max(time)<=slots[num]:
               time.append(time[-1]+np.random.exponential(1));
               
# =============================================================================
#           #The energy arrives by a poisson process 
#           energy=[];         #stores the cummulative energy accounting updates                     
#           energy.append(1);  
#           
#           #stores the cummulative energy till the epoch in which energy>=1
#           sum_en=0;
#           
#           energy_A=[];
#           
#           #Array to store scheduled status updates time
#           time_len=[];
#           
#           #Array to store actual updates time
#           time_s1=[];
#           
#           for i in range(0,len(time)):
#                sum_en=sum_en+np.random.exponential(1);
#                energy.append(sum_en);
#                
#                if sum_en>=1:
#                     energy_A.append(sum_en);
#                     sum_en=0;
#                     time_len.append(time[i]);
#           
#           samp_sum=0;
#           
#           for i in range(0,len(time)):
#                samp_sum=samp_sum+energy[i];
#                if samp_sum>=1:
#                     samp_sum=samp_sum-1;
#                     toss=np.random.binomial(1,p);
#                     if toss==1:
#                         time_s1.append(time[i]); 
#                          
# =============================================================================
          
          #energy arrives by a poisson process 
          en=0; # Instantaneous energy at instant t
          inst=[];
          
          energy=np.zeros((1,len(time))); # t-th index Stores cumulative energy till time t
          
          energy[0,0]=1;
          
          up_time=[];
          
          for i in range(1,len(time)):
               en=np.random.poisson();    # Poisson energy generated
               inst.append(en);
               energy[0,i]=en+energy[0,i-1];     
               
               if(energy[0,i]>=1):
                    energy[0,i]=energy[0,i]-1;  # Update considered and resultant energy left is updated
                    toss=np.random.binomial(1,p);
                    if(toss==1):
                         
                         up_time.append(time[i]);

          
          #variable to store age
          age=0;
          
          
          for i in range(0,len(up_time)-1):
               age=age+(np.square(up_time[i+1]-up_time[i])/2);
                
              
          age=age+(np.square(slots[num]-max(up_time))/2);
           
           
          age_list.append(age/slots[num]);

     age_list2.append(np.mean(age_list));


cong=np.zeros((1,len(slots)));     
cong[:]=(2-p)/(2*p);  
cong=np.transpose(cong);   
plt.ylim(0,6);
plt.xlabel("time",color='blue');
plt.ylabel("Time Average AoI",color='blue');
plt.plot(slots,age_list2);

plt.plot(slots,cong,'g--');
plt.legend(['sample average p=0.6','lower bound p=0.6']);
#plt.ylim(0,7);
plt.grid(True,alpha=0.8);
plt.show();      
      

     
     
     