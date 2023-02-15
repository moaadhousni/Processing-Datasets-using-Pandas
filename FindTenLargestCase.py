import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df=pd.read_csv('total_death_case.csv')

tenlargestcases=df.nlargest(10, 'cases')
cases=tenlargestcases[['state','cases']]
print(cases)
cases.to_csv('ten_largest_case.csv')

#HISTOGRAM

#cases=tenlargestcases['cases']
#state=tenlargestcases['state']

#plt.hist(cases, bins=10, edgecolor='black')


#plt.title('Number of Cases by States')
#plt.xlabel('States')
#plt.ylabel('Number of Cases')

#plt.tight_layout()

#plt.show()



