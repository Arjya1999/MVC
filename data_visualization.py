import pandas as pd
from config import ConfigProduction

class DataVisualization:
        
    def __init__(self):
        config_instance = ConfigProduction()
        self.dataset = pd.read_csv(config_instance.dataset)
        
    def histogram(self,column_name):
        
        data= self.dataset[column_name].tolist()
        
        return {'x_data':data,'y_data':[],  'type1': 'scatter', 'type2': 'histogram'}
    
    def boxplot(self,column_name):
        
        data= self.dataset[column_name].tolist()
                
        dic={"data":data}

        return dic
     
    def linechart(self,column_name1,column_name2):
        
        x_axis = self.dataset[column_name1].tolist()
        y_axis = self.dataset[column_name2].tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}

        return dic
    
    def scattergraph(self,column_name1,column_name2):
        
        x_axis = self.dataset[column_name1].tolist()
        y_axis = self.dataset[column_name2].tolist()
        data=[]
        
        for i in range(len(x_axis)):
            data.append([x_axis[i],y_axis[i]])

        return {"x_data":data, "y_data":[],'type':"scatter"}
    
    def graph_for_column_relation_with_target_variable(self,column_name):
        
        y_axis = self.dataset.corrwith(self.dataset[column_name]).tolist()
        x_axis = self.dataset.corrwith(self.dataset[column_name]).index.tolist()
            
        dic={"x_axis":x_axis,"y_axis":y_axis}

        return dic
    
    def data_completeness(self):
        
        length=len(self.dataset)
        null_data= self.dataset.isnull().sum()
        
        null_data=length-null_data
        
        x_axis =null_data.index.tolist()
        y_axis =null_data.tolist()
        
        dic={"x_data":x_axis,"y_data":y_axis}

        return dic
    
    def Bargraph(self,column_name):
        
        data= self.dataset[column_name].value_counts()
        y_axis= self.dataset[column_name].value_counts().tolist()
        x_axis = data.index.tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def heatmap_full_dataset(self):
        
        corr = self.dataset.corr()
        x_axis = corr.columns.tolist()
        y_axis = corr.values.tolist()
        
        dic={"x_axis":x_axis,"y_axis":y_axis}
    
        return dic
    
    def graph_distribution(self,column_name):
        
        data= self.dataset[column_name].tolist()
        
        dic={"data":data}

        return dic
    
    def pie_chart(self,column_name):
        temp=[]
        data = self.dataset[column_name].value_counts().tolist()
        name= self.dataset[column_name].value_counts().index.tolist()
        
        for i in range(len(data)):
            d= {"name":name[i],"y":data[i]}
            temp.append(d)
        
        return temp
    
