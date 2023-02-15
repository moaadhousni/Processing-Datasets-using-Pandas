import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#HISTOGRAM

cases=tenlargestcases['cases']
state=tenlargestcases['state']

plt.hist(cases, bins=10, edgecolor='black')


plt.title('Number of Cases by States')
plt.xlabel('States')
plt.ylabel('Number of Cases')

plt.tight_layout()

plt.show()



