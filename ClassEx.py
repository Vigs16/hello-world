class Employee(object):
    empcount=0;
    
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        Employee.empcount+=1
        self.number=Employee.empcount
        
    def Introduce(self):
        print("I am {} and my salary is {}. I am the {} employee".format(self.name,self.sal,self.number))
        

