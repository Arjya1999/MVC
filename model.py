import json

class DataHandling:
    global data
    
    f = open('sample.json',)
    
    data = json.load(f)
    
    def display(self):
        
        return data
    
    def display_by_id(self,id):
        
        return data[id]
    
    def add(self,dataset):
        data[str(len(data)+1)]=dataset
        json_object = json.dumps(data)
      
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            
        return data
    
    def delete(self,ids):
        del data[ids]
        json_object = json.dumps(data)
      
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            
        return {"msg":"The information of row "+ids+" is deleted"}
    
    def update(self,ids,name,age,gender):
        d1={}
        if name!=None:
            d1.update({"name":name})
        if age!=None:
            d1.update({"Age":age})
        if gender!=None:
            d1.update({"gender":gender})
        data.update({ids:d1})
        json_object = json.dumps(data)
      
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            
        return {"msg":"The dictionary was updated"}