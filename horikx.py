import numpy as np
import matplotlib.lines as mlines
from matplotlib import pyplot as plt
import matplotlib.pylab as pylab
from scipy.optimize import fsolve
import os
import shutil

params = {'legend.fontsize': 'xx-large',
            'figure.figsize': (16,9),
            'axes.labelsize': 'xx-large',
            'axes.titlesize': 'xx-large',
            'xtick.labelsize': 'xx-large',
            'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

si = float(input('Initial sol fraction in %: '))

si /= 100

def rand(sf,x):
    numm = 1-np.sqrt(sf)
    denn = 1-np.sqrt(si)
    return 1-(numm/denn)**2-x

def sel(sf,x):
    gi = (np.sqrt(si)-si)/(si-si**2)
    num = 1-np.sqrt(sf)
    den = 1-np.sqrt(si)
    return 1-(((np.sqrt(sf)-sf)/(sf-sf**2))/gi)*(num/den)**2-x
'''
Dresi = 210
Dressol = 
Dres = 
x = 1- (Dres-Dressol)/(Dresi-Dressol)
'''
sfSel = []
sfRand = []
x = np.linspace(0,1,num=1000)
for i in range(len(x)):
    sfSel += [fsolve(sel,x0=si,args=(x[i]))[0]-si]
    sfRand += [fsolve(rand,x0=si,args=(x[i]))[0]-si]
fig1 = plt.figure(figsize=(16,9))
plt.plot(x,sfSel,label='Selective')
plt.plot(x,sfRand,label='Random')
plt.xlim(left=0,right=1)
plt.ylim(bottom=0,top=1)
plt.ylabel(r'$S_f$')
plt.xlabel(r'$1-\nu_f/\nu_i$')
plt.title('Horikx diagram')
plt.legend()
plt.show()

if False:
    si = np.linspace(0.1,0.9,num=5)
    for i in range(len(si)):
        def sele(sf,x):
            gi = (np.sqrt(si[i])-si[i])/(si[i]-si[i]**2)
            num = 1-np.sqrt(sf)
            den = 1-np.sqrt(si[i])
            return 1-(((np.sqrt(sf)-sf)/(sf-sf**2))/gi)*(num/den)**2-x
        
        sfSel=[]
        for j in range(len(x)):
            sfSel += [fsolve(sele,x0=si[i],args=(x[j]))[0]-si[i]]
        plt.plot(x,sfSel,label='Selective'+' '+str(si[i]))
    plt.plot(x,sfRand,label='Random',color='black',linewidth=5,linestyle='dashed')
    plt.xlim(left=0,right=1)
    plt.ylim(bottom=0,top=1)
    plt.ylabel(r'$S_f$')
    plt.xlabel(r'$1-\nu_f/\nu_i$')
    plt.title('Horikx diagram')
    plt.legend()
    plt.show()

saving = input('Save? (y)es / (n)o: ')
if str(saving) == 'y':
    np.savetxt('random_'+str(si)+'.dat',np.transpose([x,sfRand]))
    np.savetxt('selective_'+str(si)+'.dat',np.transpose([x,sfSel]))
    fig1.savefig('diagram.png')
