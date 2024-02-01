from Graph import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileNamev
        self.data = []
        self.lineNumber =0
    #end def    
    def readFile(self, lineStart):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart:
                lineNumber = int(line)                
                for i in range(lineNumber): 
                    line = f1.readline()                    
                    listValue = re.sub("\s+"," ",line.strip()).split(" ")                
                    row =[]
                    for j in range(len(listValue)):                        
                        row.append(int(listValue[j]))
                    self.data.append(row)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def clear(self):
        self.data =[]
        self.lineNumber = 0
#####################            
m = Main("input.txt")
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
choice = int(input("Your selection (1->3)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(2)
    from Q3_1 import Q3_1
    q3_1 = Q3_1()
    q3_1.f1(m.data,1)
elif choice ==2:
    m.clear()
    from Q3_2 import Q3_2
    q3_2 = Q3_2()
    m.readFile(13)
    q3_2.f2(m.data,1)
elif choice==3:
    m.clear()
    from Q3_3 import Q3_3
    q3_3 = Q3_3()
    m.readFile(22)
    q3_3.f3(m.data,0,4)    
else:
    print("Wrong select")
print("FINISH")    