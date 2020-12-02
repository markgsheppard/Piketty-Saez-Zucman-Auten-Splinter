#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:02:52 2020

@author: ivnagpal
"""

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

 psz_url = 'http://gabriel-zucman.eu/files/PSZ2018MainData.xlsx'
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

df = df_merge()
