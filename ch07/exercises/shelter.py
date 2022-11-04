
class Animal: 
  def__init__(self,name,type):
    self.id = time.strftime("%d%m%M%S")
    self.id= self(id)
    self.name= name
    self.type=type
    self.arrived=time.strftime("%d/%m/%Y")
    self.adopted= None

  def set_adopted(self):
      self.adopted = time.strftime("%d/%m/%Y")

  def __str__():
      result_str= f"{sef.name}[{self.type}]"
      result_str +=f"\narrived:{self.arrived}"
      result_str 

def main():
  bruno= Animal("bruno","cat")
  bruno.set_adopted