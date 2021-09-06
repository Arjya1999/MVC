# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:50:46 2021

@author: ARJYA
"""
import pandas as pd

class DataVisualization:
        
    def __init__(self):
        self.dataset = pd.read_csv("mlb_players.csv")
    
    def histogram(self,column_name):
        
        data= self.dataset[column_name].value_counts()
        y_axis= self.dataset[column_name].value_counts().tolist()
        x_axis = data.index.tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def linechart(self,column_name1,column_name2):
        
        data_1 = self.dataset[column_name1].tolist()
        data_2 = self.dataset[column_name2].tolist()
        
        dic={"x_axis":data_1,"y_axis":data_2}

        return dic