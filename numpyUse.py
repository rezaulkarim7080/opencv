# numpy , matplotlib 

import matplotlib.pyplot as plt
import numpy as np

# import matplotlib as mpl
# Your NumPy code here

# a = np.array([1,2,3,4,5])
# print(a)

# a = np.zeros(2)
# print(a)# array([1., 1.])


# a = np.ones(2)
# print(a)# array([1., 1.])



# b = np.arange(1,10)
# b = np.arange(1,10,2)
# print(b)

# b = np.arange(5,10,dtype="complex")
# print(b)


# GRAPH GENERATE -------------with matplotlib--------

#data = {'c':20, 'C++':15,'java':40,'pyhron':15,'javascript':25}

#courses = list(data.keys())
#values = list(data.values())

#fig = plt.figure(figsize=(10,5))

#plt.bar(courses,values,color='blue',width=0.5)

#plt.xlabel("courses offered")
#plt.ylabel("No of student enrolled")
#plt.title("student menegmaent")
#plt.show()

# ----------------------------------



# --------------- PANDAS-------------

import pandas as pd
file_path = 'weather.csv'
df = pd.read_csv(file_path)



df = pd.read_csv('weather.xlsx')

df["Data.Temperature.Max Temp"].max()

print(df)



















