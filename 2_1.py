import Person
import sys

class Student(Person.Person):
    def __init__(self,name,id,gender,weight,department):
        super().__init__(name,id,gender,height,weight,department)
        self.department = department
    def showInfo(self):
        print(self.name,self.id,self.department)


if __name__ == "__main__":
    if len(sys.argv) > 6:
        Studentxxx = Student(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
        Studentxxx.showInfo()
        newID = input("new student ID:")
        newname = input("new student Name")
        newDepartment  = input("new department")
        Student.setId(newID)
        Student.setName(newname)
        Student.setDepartment(newDepartment)
        Student.showInfo()









                                                                                                                                         

