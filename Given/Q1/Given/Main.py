from MyList import *
from Car import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = None
    #end def    
    def readFile(self, lineStart, numberline):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart+1:                
                listName = re.sub('\s+',' ',line.strip()).split(" ")
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline:                 
                b = []                
                listValue = re.sub('\s+',' ',line.strip()).split(" ")
                for i in range(len(listValue)):
                    b.append(int (listValue[i]))
                self.data.append(b)
        f1.close()
    #end def       
    def creatList(self,linkList,begin=0, end=0):
        self.readFile(begin, end)  
        from Q1_1 import Q1_1        
        q11 = Q1_1()
        for i in range(len(self.data[0])):
            q11.f1(linkList,m.data[0][i],m.data[1][i])           
#####################            
m = Main("input.txt")
linkList = MyList()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1: 
    linkList.clear() 
    m.creatList(linkList,1,2)
    linkList.traverse()
elif choice ==2:
    from Q1_2 import Q1_2; q12 = Q1_2()  
    linkList.clear()
    m.creatList(linkList,4,2)
    linkList.traverse()
    q12.f2(linkList,"X",1)    
    linkList.traverse()
elif choice ==3:
    from Q1_3 import Q1_3; q13 = Q1_3()  
    linkList.clear()
    m.creatList(linkList,7,2)   
    linkList.traverse() 
    q13.f3(linkList)
    linkList.traverse()
elif choice==4:
    from Q1_4 import Q1_4; q14 = Q1_4() 
    linkList.clear()
    m.creatList(linkList,10,2)
    linkList.traverse()
    q14.f4(linkList)
    linkList.traverse()
else:
    print("Wrong select")
print("FINISH")    