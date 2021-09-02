import json
from config import ConfigProduction

class DataHandling:
    
    def __init__(self):
        f = open(ConfigProduction["db_name"],)
        
        self.data = json.load(f)
    
    def display(self):
        
        return self.data
    
    def display_by_id(self,id):
        
        return self.data[id]
    
    def add(self,dataset):
        self.data[str(len(self.data)+1)]=dataset
        json_object = json.dumps(self.data)
      
        with open(ConfigProduction["db_name"], "w") as outfile:
            outfile.write(json_object)
            
        return self.data
    
    def delete(self,ids):
        del self.data[ids]
        json_object = json.dumps(self.data)
      
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            
        return {"message":"The information of row "+ids+" is deleted"}
    
    def update(self,ids,name,age,gender):
        d1={}
        
        if name!=None:
            d1.update({"name":name})
        if age!=None:
            d1.update({"Age":age})
        if gender!=None:
            d1.update({"gender":gender})
        
        self.data.update({ids:d1})
        json_object = json.dumps(self.data)
      
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            
        return {"message":"The dictionary was updated"}