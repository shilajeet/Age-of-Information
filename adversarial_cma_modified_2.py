import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Total number of Monte Carlo simulations
Monte_Carlo=1000;

#Total number of cells and users per cell
C=1; #Number of cells
N=100; #Numnber of users per cell

#index of users stored in an array
users=np.arange(0,N);

#Duration of blockage of a given user
delta=200;

#counter to track the length of an interval
count=0;

#list to store the average age for corresponding time slots
avg_age=[];

slots=[200,300,400,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000];

for slotno in range(0,len(slots)):
     
     sum_age=np.zeros((1,slots[slotno]));
     user_age=np.ones((N,slots[slotno]));
 
     for iterate in range(0,Monte_Carlo):
          
          #Array to store the user age
          
          
          for time in range(0,slots[slotno]):
               
               if (count==0):
                    count=count+1;
                    user_block=np.random.choice(users);
                    user_send=np.random.choice(users);
                    if(user_block==user_send):
                         for i in range(0,len(users)):
                              user_age[i,time]=user_age[i,time-1]+1;
                              
                    else:
                         user_age[user_send,time]=1;
                         for i in range(0,len(users)):
                              if(i!=user_send):
                                   user_age[i,time]=user_age[i,time-1]+1;
                                   
               elif(count==delta-1):
                    count=0;
                    user_send=np.random.choice(users);
                    if(user_block==user_send):
                         for i in range(0,len(users)):
                              user_age[i,time]=user_age[i,time-1]+1;
                              
                    else:
                         user_age[user_send,time]=1;
                         for i in range(0,len(users)):
                              if(i!=user_send):
                                   user_age[i,time]=user_age[i,time-1]+1;
                                   
               else:
                    count=count+1;
                    user_send=np.random.choice(users);
                    if(user_block==user_send):
                         for i in range(0,len(users)):
                              user_age[i,time]=user_age[i,time-1]+1;
                              
                    else:
                         user_age[user_send,time]=1;
                         for i in range(0,len(users)):
                              if(i!=user_send):
                                   user_age[i,time]=user_age[i,time-1]+1;
                              
          for time in range(0,slots[slotno]):
               
               for j in range(0,len(users)):
                    
                    sum_age[0,time]=sum_age[0,time]+user_age[j,time];
            
     avg_age.append(np.sum(sum_age)/(N*Monte_Carlo*slots[slotno]));    
                 
avg_age=np.transpose(avg_age);

avg_opt_cost=[];

# =============================================================================
# for slotno in range(0,len(slots)):
#      
#      #total number of intervals
#      K=slots[slotno]/delta;
#      
#      #OPT cost for each interval
#      cost=(np.square(delta))/2 + (N*delta);
#      
#      avg_opt_cost.append((K*cost)/(N*slots[slotno]));
# =============================================================================

                 
plt.xlabel("Slots",color='blue');
plt.ylabel("Time-averaged Average AoI(in slots)",color='blue');
plt.grid(True,alpha=0.8);
plt.ylim([0,200]);

plt.plot(slots,avg_age,marker='o',markerfacecolor='yellow',color='red');
#plt.plot(slots,avg_opt_cost,'g--');
#plt.legend(['Online policy','OPT lower bound']);
plt.title("Average AoI cost for number of users N=100 and length of interval $\Delta$ = 200");
plt.show();               
               
               
resultsdf=pd.DataFrame({"time slots":slots,"time averaged average AOI(in slots)":avg_age});
resultsdf.to_csv("Modified CMA policy.csv");                           
                         
                         



















