# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:05:16 2023

@author: nbjon
"""


import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os

os.chdir("C:\\Users\\nbjon\\Downloads")

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000

# dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 
#                                  21.5, 18, 18, 20.5, 20, 20.3, 21.5, 19, 20.4, 
#                                  22.7, 22.9, 17, 23, 23.8, 22, 21.5, 21.5]})

stat = "mean"

boot_stat = []

for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name")
    
boot_dat = pd.DataFrame({"handspans": boot_stat})

(
ggplot(boot_dat, aes(x = "handspans")) +
geom_histogram()
)

plt.hist(boot_means)
plt.title('20.3 is not small')
plt.xlabel('Handspans')
plt.ylabel('Counts')


