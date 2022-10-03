import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#total number of time slots
T=1000;

#total number of Monte Carlo simulations
Monte_Carlo=3000;

#Generate energy sequence 
array=[0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0];

#Time slots
slots=np.arange(0,T,1);
#list to store previous age
age_new=np.zeros((1,T));

print("The age of information plot is for  Normal distribution using online learning for ",Monte_Carlo," Monte Carlo simulations");
for iterate in range(0,Monte_Carlo):
     
     #Generate energy sequence (through normal distribution)
     energy=[];
     
#     for i in range(0,T):
#          energy.append(np.random.rayleigh(0.5));
# =============================================================================
#     for i in range(0,T):
#          energy.append(np.random.uniform(0,1));
# =============================================================================
          
# =============================================================================
#     for i in range(0,T):
#           energy.append(np.random.choice(array));
# =============================================================================
     
# =============================================================================
     for i in range(0,T):
           energy.append(abs(np.random.normal(0,0.1)));
# =============================================================================
     
     energy[0]=0;
     
     #variable to store sum of energy
     enr_sum=0;
     
     #list to store update times 
     update=[];
     
     #list to store age at every time slot
     age=np.ones((1,T));
     
     #Minimum age bound, max age bound and average age   
     age_min=2;
     age_max=4;
     avg_age=(age_min+age_max)/2;  
     
     #Minimum energy, maximum energy and average energy
     en_min=1;
     en_max=5;
     avg_en=(en_min+en_max)/2;
     
     #count stores the number of status updates made till time T
     count=0;
     
     for time in range(0,T-1):
          
          enr_sum=enr_sum+energy[time];
          
          #Mean energy till current time
          en_mean=enr_sum/(time+1);
          
          #Variance of energy till current time
          en_var=np.var(energy[:time+1]);
          
          #Minimum and maximum energy threshold
          en_min=en_mean+en_var*10;
          en_max=en_mean+en_var*20;
          avg_en=(en_min+en_max)/2;
          
          #Mean age till current time
          age_mean=np.mean(age[:time+1]);
          
          #Variance of age till current time
          age_var=np.var(age[:time+1]);
          
          #Minimum, maximum and average age threshold
          age_min=age_mean+age_var;
          age_max=age_mean+age_var*2;
          avg_age=(age_min+age_max)/2;
          
          if enr_sum>en_max:
               count=count+1;
               update.append(time);
               enr_sum=enr_sum-1;
               age[0,time+1]=1;
               
          elif enr_sum<en_min:
               age[0,time+1]=age[0,time]+1;
               
          elif (enr_sum>=en_min)&(enr_sum<=en_max):
               if age[0,time]>age_max:
                    count=count+1;
                    update.append(time);
                    enr_sum=enr_sum-1;
                    age[0,time+1]=1;
                    
               elif age[0,time]<age_min:
                    age[0,time+1]=age[0,time]+1;
                    
               elif (age[0,time]>=age_min)&(age[0,time]<=age_max):
                    
                    if (age[0,time]>=avg_age)&(enr_sum>=avg_en):
                         count=count+1;
                         update.append(time);
                         enr_sum=enr_sum-1;
                         age[0,time+1]=1;
                         
                    else:
                         age[0,time+1]=age[0,time]+1;
                       
     age_new=age+age_new;


print(age_new);                    
age_new=age_new/Monte_Carlo;
age_new=np.transpose(age_new);

age_exact=[];

for i in range(0,age_new.size):
     age_exact.append(age_new[i,0]);

time=[];
for j in range(0,slots.size):
     time.append(slots[j]);
     
#plots
plt.xlabel("time",color='blue');
plt.ylabel("Age of Information",color='blue'); 
plt.plot(slots,age_new);
plt.grid(True,alpha=0.8);
plt.show(); 
     
resultsdf=pd.DataFrame({"time":time,"Age of Information":age_exact});
resultsdf.to_csv("Results_of_AoI_Normal_dist_online_learning.csv");  
     
     

     