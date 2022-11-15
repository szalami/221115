class App:
    def __init__(self):                 #konstruktor
        self.fileName = 'dolgozok.txt'

    def readFile(self):                 #metódus
        fp = open(self.fileName, 'r', encoding='UTF-8')
        self.lines = fp.readlines()
        for line in self.lines:
            #print(line.rstrip()) - törli a sorvégi whitespace-eket
            pass

        fp.close()
        
    def sumSalary(self):
        sum = 0
        for line in self.lines:
           #lineArray = line.split(':')
           (id, name, city, address, salary, enter) = line.split(':')
           #print(int(salary))
           if city == 'Miskolc':                #szelektáljuk feltételek aélapján
                sum = sum + int(salary)

        print('Összeg:', sum)
          
        

app = App()                             #objektum /app/ - konstruktor meghívása
app.readFile()
app.sumSalary()