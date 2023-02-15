import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df=pd.read_csv('total_death_case.csv')

tenlargestcases=df.nlargest(10, 'deaths')
cases=tenlargestcases[['state','deaths']]
print(cases)
cases.to_csv('ten_largest_death.csv')

#deaths=tenlargestcases['deaths']
#state=tenlargestcases['state']

#plt.hist(deaths, bins=10, edgecolor='black')


#plt.title('Number of Deaths by States')
#plt.xlabel('Deaths')
#plt.ylabel('Number of Deaths')

#plt.tight_layout()

#plt.show()
