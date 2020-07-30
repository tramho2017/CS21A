from employee8 import Employee
class Manager(Employee):#creat subclass manager
    def __init__(self,firstName,lastName,SSN,salary,title,annualBonus):
        Employee.__init__(self, firstName,lastName,SSN,salary)
        self.title=title
        self.annualBonus=annualBonus
    def __str__(self):#this function return the name of object
            return(self.firstName+" "+self.lastName+" SSN: "+str(self.SSN)+" salary: "+str(self.salary)+" title: "+self.title+" annual bonus: "+str(self.annualBonus))







