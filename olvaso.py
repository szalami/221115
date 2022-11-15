from employee import Employee
class App:
    def __init__(self):                 #konstruktor
        self.fileName = 'dolgozok.txt'
        self.employeeList = []

    def readFile(self):                 #metódus
        fp = open(self.fileName, 'r', encoding='UTF-8')
        lines = fp.readlines()

        for line in lines:
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

  #számoljuk meg a miskolciakat        
    def countMiskolc(self):
        count = 0
        for employee in self.employeeList:
            if employee.city == 'Miskolc':
                count = count + 1
        print("Miskolciak: ", count)  

    # irassa ki a Szolnoki dolgozók neveit és fizetésüket
    def printSzolnokDatas(self):
        print("Szolnokiak:")
        for employee in self.employeeList:
            if employee.city == 'Szolnok':
                print(employee.name, employee.salary)

app = App()                           #objektum /app/ - konstruktor meghívása
app.readFile()
app.sumSalary()
app.countMiskolc()
app.printSzolnokDatas()




