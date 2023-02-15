import pandas as pd
import json

df=pd.read_csv('us-counties.csv')
print(df)

df.to_json(r'jsonfile.json')

newdf=pd.read_json(r'jsonfile.json')
print(newdf)


