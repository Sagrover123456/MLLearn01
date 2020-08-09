import pyodbc
import sqlalchemy
import pandas as pd
import requests
import datetime
from datetime import date, timedelta
import warnings
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
df  = pd.read_csv(r'C:\Users\sagrover\Documents\Sanyogita\Documents\Python Scripts\ML\Salaries.csv')
df1  = pd.read_csv(r'C:\Users\sagrover\Documents\Sanyogita\Documents\Python Scripts\ML\Salaries.csv')
# df['length_title'] = df['Job_Title'].apply(len)
for col in df.columns: 
    print(col) 
df['length_title']=df['JobTitle'].apply(len)
df[['length_title','TotalPayBenefits']].corr()
## plot making
x = np.linspace(0,5,10)
y= x**2
plt.plot(x,y,'b')
# plt.show()

### Object Oriented
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plt(x,y,r)
axes.set_title('Object Oriented')
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.3,0.4,0.2]) #left,bottom,width,height
axes1.plt(x,y,r)
axes2.plt(x,y,r)
# plt.show()

