class Q1_3:
    def f3(self, linkList):
        if self.check(linkList.head.data.Price):
            linkList.head = linkList.head.next
        else:            
            cu = linkList.head
            while(cu.next):
                if (self.check(cu.next.data.Price)):                    
                    break
                cu = cu.next
            if (cu.next==None): 
                return
            else:
                if (cu.next==linkList.tail):
                    linkList.tail=cu    
                cu.next = cu.next.next
              
    def check(self, x):
        return x==5