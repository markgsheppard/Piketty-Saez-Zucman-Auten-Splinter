import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import urllib
import time

from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import make_interp_spline, BSpline
from scipy import interpolate

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import gridplot
from bokeh.models import HoverTool, SingleIntervalTicker, LinearAxis
from ipywidgets import interact
from bokeh.io import output_notebook
output_notebook()


#URL for Piketty, Saez, and Zucman Income Inequality Dataset
psz_url = 'http://gabriel-zucman.eu/files/PSZ2018MainData.xlsx'

#URL for Auten and Splinter Income Inequality Dataset
as_url = 'http://davidsplinter.com/AutenSplinter-IncomeIneq.xlsx'

def df_merge (psz_url, as_url):
    s_1 = time.time()  #Start time for data download
    e_1 = time.time()  #End time for data download
    urllib.request.urlretrieve(psz_url, "piketty-saez-zucman.xlsx")
    urllib.request.urlretrieve(as_url, "auten-splinter.xlsx")
    print("Data Downloaded in", (e_1 - s_1), "seconds.")
    s_2 = time.time()  #Start time for data cleaning
    e_2 = time.time()  #End time for data cleaning
    psz_df = pd.read_excel(psz_url, 'Data', usecols=('A:AN, AQ:BJ, BM:CY, DB:EO, EQ:FY, GA:GN, GQ:HD, HG:HR, HT:IM, IO:IP, IS:JE, JG:JO'), 
                           header=[2]).drop([0,1]).rename(columns={"Series": "Year"})
    psz_df.drop(psz_df.tail(11).index,inplace=True)
    as_df = pd.read_excel(as_url, 'F-A1', header=[32], usecols=('A:E, G:J')).rename(columns={'Unnamed: 0': "Year"}).drop([56,57])
    print("Data cleaned in", (e_2 - s_2), "seconds.")
    df = psz_df.merge(as_df, how='outer')
    print("Merge complete")
    return df

df = df_merge(psz_url,as_url)


def hover_graph ():
    hover = HoverTool(
        tooltips= """
        <div style="background-color: rgba(0, 0, 0, 0.0);>
            <div style="background-color: rgba(2, 0, 0, 0.0);>
                <span style="font-size: 8px;">Year</span>
                <span style="font-size: 8px; color: #7c7c7c;">$x{2f}</span>
                </br>
                <span style="font-size: 8px;">Value</span>
                <span style="font-size: 8px; color: #7c7c7c;">$y{2f}%</span>
            </div>
        </div>
        """
    )
    plot = figure(x_axis_label='Year', 
                  y_axis_label='Share of National Income', tools=[hover], 
                  plot_width=800, plot_height=500, title="Top 10% Share of National Income")
    plot.outline_line_color = None
    plot.xaxis.major_tick_line_color = None  
    plot.yaxis.major_tick_line_color = None
    plot.xaxis.minor_tick_line_color = None  
    plot.yaxis.minor_tick_line_color = None
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_dash = [2, 2]
    plot.yaxis.axis_line_color = "White"
    plot.xaxis.axis_line_color = "#7c7c7c"
    year = list(df['Year'])
    psz_top10 = list(df['Memo: Top 10% fiscal income per tax unit, incl. KG'].fillna(df['Memo: Top 10% fiscal income per tax unit, incl. KG']
                                                                                 .mean()))
    as_top10 = list(df['Pre-tax after-transfer income'].fillna(df['Pre-tax after-transfer income']
                                                                                 .mean()))
    xnew = np.linspace(min(year), max(year), 300)
    psz_spl = make_interp_spline(year, psz_top10, k=3)
    as_spl = make_interp_spline(year, as_top10, k=3)
    psz_smooth = psz_spl(xnew)
    as_smooth = as_spl(xnew)
    plot.line(xnew[:-2], psz_smooth[:-2]*100, line_width=1.5, color='#9ebed2', legend_label="Piketty, Saez, & Zucman", 
              muted_alpha=0.2)
    plot.line(xnew[130:-2], as_smooth[130:-2]*100, line_width=1.5, color="#5787ae", legend_label="Auten & Splinter",
              muted_alpha=0.2)
    plot.xaxis.ticker = SingleIntervalTicker(interval=10)
    plot.yaxis.ticker = SingleIntervalTicker(interval=2)
    plot.legend.border_line_width = 0
    plot.legend.title = 'Researchers'
    plot.legend.title_text_font_style = "bold"
    plot.legend.title_text_font_size = "15px"
    plot.legend.label_text_font_size = "10px" 
    plot.legend.location = "bottom_left"
    plot.legend.click_policy="mute"
    output_file("Sample.html")
    save(plot)

#Call hover_graph function
hover_graph()
