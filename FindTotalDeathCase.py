import pandas as pd
def top_bystate():
	df=pd.read_csv('specified_day_output.csv')
	find_top_bystate=df.groupby('state')
	summation=find_top_bystate.sum()
	sum=summation[['cases','deaths']]
	print(sum)

	sum.to_csv('total_death_case.csv')

top_bystate()