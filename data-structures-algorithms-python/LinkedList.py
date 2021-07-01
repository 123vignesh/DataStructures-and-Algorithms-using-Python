#Singly Linked list
#add at begining
#add at end
#add at given position
#delete at given position
#add list elements to linkedlist
#add by value after a value in linkedlist
#delete by value

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_List:
    def __init__(self,head=None):
        self.head=head        

    def to_print(self):
        stri=""
        t=self.head
        while(t):
            stri=stri+str(t.data)+" --->"
            t=t.next
        return stri

    def to_add_at_begining(self,data):
        if(self.head==None):
            self.head=Node(data)
            return self.to_print()
        else:
            node=Node(data,self.head)
            self.head=node
            return self.to_print()

    def to_add_at_end(self,data):
        if(self.head==None):
            self.head=Node(data)
            return self.to_print()
        else:
            t=self.head
            while(t):
                if(t.next==None):
                    break
                t=t.next
            t.next=Node(data)
            return self.to_print()

    def add_at(self,index,data):
        if(index==1):
            return self.to_add_at_begining(data)
        else:
            t=self.head
            count=1
            while(t):
                if(count==index-1):
                    break

                count=count+1 
                t=t.next
            print(t.data)    
            t.next=Node(data,t.next)
            return self.to_print()

    def del_at(self,index):
        if(index==1):
            self.head=self.head.next
            return self.to_print()
        else:
            count=1
            t=self.head
            a=0
      
        
            while(t):
                if(count==index-1):
                    a=t
                    break
                
                t=t.next
                count=count+1   
            a.next=a.next.next
            return self.to_print()     
    
    def add_list(self,array):
        for i in array:
            self.to_add_at_end(i)
        return self.to_print()

    def add_by_value(self,after_which,value):
        t=self.head
        while(t):
            if(t.data==after_which):
                break
            t=t.next
        t.next=Node(value,t.next)
        return self.to_print()    

    def del_by_value(self,value):
        if(self.head.data==value):
            self.head=self.head.next
            return self.to_print()
        t=self.head
        a=0
        while(t):
            if(t.next.data==value):
                t.next=t.next.next
                return self.to_print()
                


            t=t.next


li=Linked_List()




print(li.add_list(["mango","apple","grapes"]))

print(li.add_by_value("grapes","orange"))

print(li.del_by_value("orange"))


                        