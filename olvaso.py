from employee import Employee
class App:
    def __init__(self):                 #konstruktor
        self.fileName = 'dolgozok.txt'
        self.employeeList = []

    def readFile(self):                 #metódus
        fp = open(self.fileName, 'r', encoding='UTF-8')
        self.lines = fp.readlines()

        for line in self.lines:
            (id, name, city, address, salary, birth) = line.split(':')
            employee = Employee(id, name, city, address, salary, birth)
            self.employeeList.append(employee)
            #print(line.rstrip()) - törli a sorvégi whitespace-eket

        fp.close()
        
    def sumSalary(self):
        sum = 0
        for employee in self.employeeList:
           #print(int(salary))
           if employee.city == 'Miskolc':                #szelektáljuk feltételek aélapján
                sum = sum + int(employee.salary)

        print('Összeg:', sum)
          
        

app = App()                           #objektum /app/ - konstruktor meghívása
app.readFile()
app.sumSalary()