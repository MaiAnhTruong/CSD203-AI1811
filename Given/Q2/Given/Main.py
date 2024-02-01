from BSTree import *
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
                listName = re.sub("\s+"," ",line.strip()).split(" ")                
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline: 
                listValue = re.sub("\s+"," ",line.strip()).split(" ")
                b =[]
                for i in range(len(listValue)):
                    b.append(int(listValue[i]))
                self.data.append(b)
        f1.close()
    # def display(self):
    #     for line in self.data:
    #         print(line, end ="\n")        
    #             # listName = line.strip().split(", ")
    # def f1(self, tree):
    #     for i in range(len(self.data[0])):           
    #         tree.insert(self.data[0][i],self.data[1][i])
    # #end def       
    def createTree(self,tree,begin=0, end=0):
        from Q2_1 import Q2_1; q21 = Q2_1()
        self.readFile(begin, end)
        for i in range(len(self.data[0])):
            q21.f1(tree,self.data[0][i],self.data[1][i])
#####################            
m = Main("input.txt")
tree = BSTree()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1:  
    m.createTree(tree,1,2)
    tree.preVisit()    
    tree.inVisit()    
elif choice ==2:
    from Q2_2 import Q2_2
    q22 = Q2_2()
    tree.clear()    
    m.createTree(tree,4,2)  
    tree.preVisit()  
    q22.f2(tree)
elif choice ==3:
    tree.clear()
    m.createTree(tree,7,2)
    from Q2_3 import Q2_3
    q23 = Q2_3()
    tree.breadth_first()   
    q23.f3(tree)
    tree.breadth_first()
elif choice==4:
    tree.clear()
    from Q2_4 import Q2_4
    q24 = Q2_4()
    m.createTree(tree,10,2)
    tree.breadth_first()    
    q24.f4(tree)
    tree.breadth_first()    
else:
    print("Wrong select")
print("FINISH")    