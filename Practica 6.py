#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10, 10)  #set default figure size
def stationary_state(β,α,δ,A):
    k_stationary= round((((1/β)-1+δ)/(α*A))**(1/(α-1)),3)
    c_stationary= round((A*(k_stationary)**α)+(-δ*k_stationary),3)
    r=round(α*A*k_stationary**(α-1)+1-δ,6)
    return k_stationary, c_stationary, r
k_stationary, c_stationary, r=stationary_state(0.99,0.34,0.02,1)
print("K estacionario es: "
      + str(k_stationary)
      +" y C estacionario es: "
      +str(c_stationary)
      +" el retorno r es: "
      +str(r))


# In[2]:


k_stationary1, c_stationary1, r1=stationary_state(0.99,0.34,0.02,1.05)
print("K estacionario nuevo es: "
      + str(k_stationary1)
      +" y C estacionario nuevo es: "
      +str(c_stationary1)
      +". El nuevo retorno r es: "
      +str(r1))


# In[3]:


def P(β,α,δ,A,k):
    A0=round(-(α*A*k**(α-1)+1-δ),1)
    A1=round((1+α*A*k**(α-1)+1-δ+β*(A*k**α-δ*k)*α*(α-1)*A*k**(α-2)),3)
    P1=round((A1+(A1**2+4*A0)**(1/2))/2,3)
    P2=round((A1-(A1**2+4*A0)**(1/2))/2,3)
    return P1, P2, A0, A1
P(0.99,0.34,0.02,1.05,k_stationary1)
P1,P2,A0,A1=P(0.99,0.34,0.02,1.05,k_stationary1)
A0,A1,P1,P2,print("vemos que P1>1 es: "+ str(P1>1)+ " y que P2>1 es: "+ str( P2>1))    
    


# In[4]:


khat0= np.log(k_stationary/k_stationary1)
α=0.34
A=1.5
t=216
t_lenght=np.linspace(0,t,t)
deviationk=np.zeros((t,1))
k_evolution=np.zeros((t,1))
w_evolution=np.zeros((t,1))
r_evolution=np.zeros((t,1))
for t in range(0,t):
    if t==0:
        deviationk[0,0]=khat0
        k_evolution[0,0]=np.exp(deviationk[0,0])*k_stationary1
        w_evolution[0,0]=(1-α)*A*k_evolution[0,0]**α
        r_evolution[0,0]=α*A*k_evolution[0,0]**(α-1)
    else:
        deviationk[t,:]=deviationk[t-1,0]*P2
        k_evolution[t,:]=np.exp(deviationk[t,0])*k_stationary1
        w_evolution[t,:]=(1-α)*A*k_evolution[t,0]**α
        r_evolution[t,:]=α*A*k_evolution[t,0]**(α-1)


fig, ([ax1,ax2],[ax3,ax4])= plt.subplots(2,2)
fig.subplots_adjust(hspace = 0.25, wspace=.25)
ax1.plot(t_lenght, deviationk[:,0])
ax2.plot(t_lenght,k_evolution[:,0])
ax3.plot(t_lenght,w_evolution[:,0])
ax4.plot(t_lenght,r_evolution[:,0])
ax1.set(xlabel="time",ylabel="log Deviation")
ax2.set(xlabel="time",ylabel="K Evolution")
ax3.set(xlabel="time",ylabel="Wages Evolution")
ax4.set(xlabel="time",ylabel="K Price")

plt.show()

