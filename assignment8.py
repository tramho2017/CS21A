from manager8 import Manager
from employee8 import Employee
from operator import attrgetter

if __name__ == "__main__":
    employee=Employee("tram","ho",123452325,1000)
    employee1=Employee('tram','ho',364783267,2000)
    print(employee.__eq__(employee1))


    employee2=Employee("anhhj","ho",123452325,1000)
    employee3=Employee('nah','tran',364783267,2000)

    manager1=Manager("mary", "edwin",475876338,2000, "officer", 3456 )
    manager2=Manager('john','edwin', 456728934,3000, "clerk", 4567)

    print(employee2.__eq__(employee3))

    print (employee2.__lt__(employee3))

    print(manager1.__lt__(manager2))

    employee4 = Employee('tram', 'tran', 897456278, 2000)
    employee5 = Employee('mai', 'ho', 364783267, 2000)
    manager3 = Manager("mary", "edwin", 475876338, 2000, "clerk", 1234)
    manager4 = Manager("john", "Cunning", 355687654, 2000, "officer", 3456)

    list=[employee4,employee5,manager3,manager4]
    sortlist=sorted(list, key=attrgetter("lastName"))
    print(sortlist)

print(employee4==employee5)
print(employee1<employee2)
print(employee1>employee2)
print(manager3<manager4)