import math
from Stack import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def depthFirst(self,start):
        b = [True]*len(self.a)
        b[start] = False    
        self.depth(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth(i,b)
    def depth(self,start,b):
        t = self.deg(start)
        print(f"{chr(start+65)}", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth(i,b)
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count
    #----------------------------
    def f1(self,start):
        self.depthFirst(start)
        print("")
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1========



        #---------------------------
        print("")
    
    #----------------------------    
    '''Algorithm for finding an Euler cycle from the vertex X using stack 
//Input: Connected graph G with all vertices having even degrees
//Output: Euler cycle
declare a stack S of characters
declare empty array E (which will contain Euler cycle)
push the vertex X to S
while(S is not empty)
 {r = top element of the stack S 
  if r is isolated then remove it from the stack and put it to E
   else
   select the first vertex Y (by alphabet order), which is adjacent
   to r, push  Y  to  S and remove the edge (r,Y) from the graph   
 }
 the last array E obtained is an Euler cycle of the graph'''
    #-------------------------------------
    def f2(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========




        #------------------------------
        print("")
        

    # -----------------------------
    def f3(self,start,end):
        
        pass
