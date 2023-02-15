import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#HISTOGRAM

deaths=tenlargestcases['deaths']
state=tenlargestcases['state']

plt.hist(deaths, bins=10, edgecolor='black')


plt.title('Number of Deaths by States')
plt.xlabel('Deaths')
plt.ylabel('Number of Deaths')

plt.tight_layout()

plt.show()