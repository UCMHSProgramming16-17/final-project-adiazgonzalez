#import csv
#import requests
import pandas as pd 

df = pd.read_csv('moves.csv')

from bokeh.charts import Bar, Scatter, output_file, save


df =df[df['power'] != '—']

print(df)

pokebar= Bar(df, 'type', values='power', agg = 'count', title= "Number of Moves per Type")

pokescatter= Scatter(df, x= "pp", y="power", title= "Power Relative to PP of Pokemon Moves")

output_file('pokebar.html')
save(pokebar)

output_file('pokescatter.html')
save(pokescatter)