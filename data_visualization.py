# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:50:46 2021

@author: ARJYA
"""
import pandas as pd
import seaborn as sns

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
    
    def scattergraph(self,column_name1,column_name2):
        
        data_1 = self.dataset[column_name1].tolist()
        data_2 = self.dataset[column_name2].tolist()
        
        dic={"x_axis":data_1,"y_axis":data_2}

        return dic
    
    def graph_for_column_relation_with_target_variable(self,column_name):
        
        y = self.dataset.corrwith(self.dataset[column_name]).tolist()
        x = self.dataset.corrwith(self.dataset[column_name]).index.tolist()
            
        dic={"x_axis":x,"y_axis":y}

        return dic
    
    def data_completeness(self):
        
        length=len(self.dataset)
        null_data= self.dataset.isnull().sum()
        
        null_data=length-null_data
        
        x=null_data.index.tolist()
        y=null_data.tolist()
        
        dic={"x_axis":x,"y_axis":y}

        return dic
    
    def Bargraph(self,column_name):
        
        data= self.dataset[column_name].value_counts()
        y_axis= self.dataset[column_name].value_counts().tolist()
        x_axis = data.index.tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def heatmap_full_dataset(self):
        
        corr = self.dataset.corr()
        x = corr.columns.tolist()
        y = corr.values.tolist()
        
        dic={"x_axis":x,"y_axis":y}
    
        return dic
    
    def graph_distribution(self,column_name):
        
        data = sns.distplot(self.dataset[column_name]).get_lines()[0].get_data()
        
        x_axis= data[0].tolist()
        y_axis= data[1].tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def skewness(self,column_name):
        
        data = sns.distplot(self.dataset[column_name]).get_lines()[0].get_data()
        
        x_axis= data[0].tolist()
        y_axis= data[1].tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def boxplot(self,column_name):
        
        ax = sns.boxplot(data= self.dataset[column_name])
        
        pass
    