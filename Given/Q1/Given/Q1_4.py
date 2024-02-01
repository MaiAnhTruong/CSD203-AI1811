class Q1_4:
    def f4(self,linkList):
        if linkList ==None:
            return
        i = linkList.head
        while (i.next):
            j = i.next
            while j:
                if i.data.Price > j.data.Price:
                    t = i.data
                    i.data = j.data
                    j.data = t
                j= j.next
            i = i.next        