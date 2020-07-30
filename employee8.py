from functools import total_ordering
@total_ordering
class Employee: # creat BaseClass Employee

    def __init__(self,firstName,lastName,SSN,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.SSN=SSN
        self.salary=salary

    def __str__(self):
        print(self.firstName+" " +self.lastName+" "+ str(self.SSN)+" "+str(self.salary))
        return (self.firstName +" "+self.lastName + " SSN: "+ str(self.SSN)+ " salary: "+str(self.salary))


    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Returns True if firstname(self)=firstname(other), lastname(self)=lastname(other), return False otherwise
        """
        if self.firstName == other.firstName and self.lastName == other.lastName:
            return True
        else:
            return False


    def __lt__(self, other):
        """
        This method must return True when the name in self is alphabetically less than the name in other, and return False otherwise.
        If the last names are equal, this method must check the first names to determine which object is less than the other.
        :param other:
        :return:
        """
        if self.lastName < other.lastName:
            return True
        elif self.lastName == other.lastName:
            if self.firstName < other.firstName:
                return True
        return False