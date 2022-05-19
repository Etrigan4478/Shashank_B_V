#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[2]:


D = pd.read_csv("play.csv")


# In[4]:


con = np.array(D)[:,:-1]
con


# In[5]:


tar = np.array(D)[0:5,-1:]
tar


# In[7]:


def candidate(con, tar): 
    spec_h = con[0].copy()
    print("\nSpecific Boundary: ", spec_h)
    gen_h = [["?" for i in range(len(spec_h))] for i in range(len(spec_h))]
    print("\nGeneric Boundary: ",gen_h)  

    for i, h in enumerate(con):
        print("\nInstance", i+1 , "is ", h)
        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(spec_h)): 
                if h[x]!= spec_h[x]:                    
                    spec_h[x] ='?'                     
                    gen_h[x][x] ='?'
                   
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(spec_h)): 
                if h[x]!= spec_h[x]:                    
                    gen_h[x][x] = spec_h[x]                
                else:                    
                    gen_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", spec_h)         
        print("Generic Boundary after ", i+1, "Instance is ", gen_h)
        print("\n")

    indices = [i for i, val in enumerate(gen_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        gen_h.remove(['?', '?', '?', '?', '?', '?']) 
    return spec_h, gen_h 

s_final, g_final = candidate(con, tar)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")


# In[ ]:





# In[ ]:





# In[ ]:




