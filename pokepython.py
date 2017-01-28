#import csv
#import requests
import pandas as pd 

df = pd.read_csv('moves.csv')

from bokeh.charts import Bar, output_file, save


df =df[df['power'] != '—']

print(df)

pokebar= Bar(df, 'type', values='power', agg = 'count', title= "Amount of Moves per Type")

output_file('pokebar.html')
save(pokebar)