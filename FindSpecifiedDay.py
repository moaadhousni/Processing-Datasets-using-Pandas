import pandas as pd
#specified date is March 31 2020

def specified_day():
	df=pd.read_csv('us-counties.csv')
	specified_day_output = df[['date', 'state', 'cases','deaths']]
	date=str(input('date'))
	specified_day_output = specified_day_output[(specified_day_output['date']== date)]

	print(specified_day_output)
	specified_day_output.to_csv('specified_day_output.csv')

specified_day()