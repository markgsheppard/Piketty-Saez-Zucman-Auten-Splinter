import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import urllib

from bokeh.plotting import figure, show 
from bokeh.layouts import gridplot
from bokeh.models import HoverTool
from ipywidgets import interact
from bokeh.io import output_notebook
output_notebook()

path = '/Users/marksheppard/Documents/GitHub/Python Project/'
psz_url = 'http://gabriel-zucman.eu/files/PSZ2018MainData.xlsx'
as_url = 'http://davidsplinter.com/AutenSplinter-IncomeIneq.xlsx'

path = '/Users/marksheppard/Documents/GitHub/Python Project/'

psz_url = 'http://gabriel-zucman.eu/files/PSZ2018MainData.xlsx'
as_url = 'http://davidsplinter.com/AutenSplinter-IncomeIneq.xlsx'

psz_xls = pd.ExcelFile('piketty-saez-zucman.xlsx')
as_xls = pd.ExcelFile("auten-splinter.xlsx")
psz_df = pd.read_excel(psz_xls, 'Data')
as_df = pd.read_excel(as_xls, 'F-A1')

new_as_header = as_df.iloc[31] #grab the first row for the header
as_df = as_df[32:] #take the data less the header row
as_df.columns = new_as_header #set the header row as the df header
as_df.columns = as_df.columns.fillna('Year')
as_df.drop(as_df.tail(2).index,inplace=True)
#as_df = as_df.reset_index()
#as_df = as_df.drop(as_df.columns[6], axis=1)
#as_df.head()

new_psz_header = psz_df.iloc[1] #grab the first row for the header
psz_df = psz_df[2:] #take the data less the header row
psz_df.columns = new_psz_header #set the header row as the df header
psz_df = psz_df.rename(columns={"Series": "Year"})
psz_df = psz_df.drop([2,3])
psz_df.drop(psz_df.tail(11).index,inplace=True)
#psz_df.tail()

psz_df.head()

#as_df = as_df.filter(['Year'])
#psz_df = psz_df.filter(['Year'])

path_ = '/Users/marksheppard/Documents/GitHub/homework-3-markgsheppard-1/'
file_name_ = [('Income.csv'),
            ('Grant.csv')]
income_df = pd.read_csv('Income.csv') 
grant_df = pd.read_csv('Grant.csv')

income_df = income_df.filter(['year', 'inst_name', 'faminc_mean', 'faminc_med'])
grant_df = grant_df.filter(['year', 'inst_name', 'type_of_aid', 'number_of_students', 'average_amount', 'total_amount'])

df = income_df.merge(grant_df)

def grant_type(type_of_aid):
    return df[df['type_of_aid']==type_of_aid]
aid = df['type_of_aid'].unique()

def school_type(type_of_school):
    return df[df['inst_name']==type_of_school]
school = df['inst_name'].unique()

df['number_of_students_scaled'] = np.abs(df['number_of_students']) / 50

plt.scatter('faminc_mean', 'average_amount', c = 'year', s ='number_of_students_scaled', alpha=0.6, data=df)
plt.xlabel('Average Financial Aid Award')
plt.ylabel('Mean Family Income')
plt.show()

plt.scatter('faminc_med', 'average_amount', c = 'year', s ='number_of_students_scaled', alpha=0.6, data=df)
plt.xlabel('Average Financial Aid Award')
plt.ylabel('Median Family Income')
plt.show()

plot = figure(x_axis_label='Mean Family Income', 
              y_axis_label='Average Amount of Aid')

plot.circle(df['faminc_med'], df['average_amount'])
#https://github.com/bokeh/bokeh/blob/branch-2.3/examples/app/crossfilter/main.py
#https://github.com/Data-and-Programming-2-TAs/Sarah-Discussion-Notebooks/blob/master/lab_5-interactive%20plotting%20example.ipynb

show(plot)


plot = figure(x_axis_label='Mean Family Income', 
              y_axis_label='Average Amount of Aid')

plot.circle(df['faminc_mean'], df['average_amount'])
#https://github.com/bokeh/bokeh/blob/branch-2.3/examples/app/crossfilter/main.py
#https://github.com/Data-and-Programming-2-TAs/Sarah-Discussion-Notebooks/blob/master/lab_5-interactive%20plotting%20example.ipynb

show(plot)

#Interactive Plots
hover = HoverTool(tooltips = [('Median Income', '@x'), ('Amount of Aid', '@y')])
plot = figure(x_axis_label='Median Family Income', 
              y_axis_label='Average Amount of Aid',
              tools=[hover])

plot.circle(df['faminc_med'], df['average_amount'])
#https://github.com/bokeh/bokeh/blob/branch-2.3/examples/app/crossfilter/main.py

show(plot)

@interact(School=school) # dropdown menue
def interactive(School=school):
    hover = HoverTool(tooltips = [('Median Income', '@x'), ('Amount of Aid', '@y')])
    plot = figure(x_axis_label='Median Family Income', 
              y_axis_label='Average Amount of Aid',
              tools=[hover])
    plot_df = school_type(School)
    plot.circle(plot_df['faminc_med'], plot_df['average_amount'])
    #https://github.com/bokeh/bokeh/blob/branch-2.3/examples/app/crossfilter/main.py
    show(plot)


