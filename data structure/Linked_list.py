class node:
  def __init__(self,data):
    self.data=data
    self.next=None

class link_list:
  def __init__(self):
    self.head=None
  
  def show(self):
    temp=self.head
    while temp is not None:
      print(temp.data)
      temp=temp.next

  
n1=link_list()

n1.head=node("Mithun")
n2=node("Suresh")
n3=node("Yamini")
n4=node("Babu")

n1.head.next=n2
n2.next=n3
n3.next=n4

# n1.head.data,n2.data,n3.data,n4.data # we can do this also but second is correct format
# n1.head.next.data # we always point from head node(i.e n1.head) beacause link list is n1
# n1.head.next.next.data
# n1.head.next.next.next.data

n1.show()





# ?-------------------------------------------------------------------------------------------------------------------------------------




class node:
  def __init__(self,data): 
    self.data=data
    self.next=None

class link_list: 
  def remove(self,removedata):
    temp=self.head
    while temp is not None:
      if temp.data==removedata:
        break
      pre_node=temp
      temp=temp.next
    if temp:
      pre_node.next=temp.next
    
    else:
      print("----------")
      print("no such a data")
      print("----------")

  def insert_beg(self,data):
    newNode=node(data)
    newNode.next=self.head
    self.head=newNode

  def insert_end(self,data):
    newNode=node(data)
    temp=self.head
    while temp.next is not None:
      temp=temp.next
    temp.next=newNode


  def insert(self,mid,data): #insert temp node in middle
    newNode=node(data)
    newNode.next=mid.next
    mid.next=newNode

  def __init__(self): #defining and creating a head node
    self.head=None
  
  def show(self): #showing all node data 
    temp=self.head
    while temp is not None:
      print(temp.data)
      temp=temp.next

  
n1=link_list()

n1.head=node("Mithun")  
n2=node("Suresh")
n3=node("Yamini")
n4=node("Babu")

n1.head.next=n2
n2.next=n3
n3.next=n4

# n1.head.data,n2.data,n3.data,n4.data # we can do this also but second is correct format
# n1.head.next.data # we always point from head node(i.e n1.head) beacause link list is n1
# n1.head.next.next.data
# n1.head.next.next.next.data
print("----before Insert----------")
n1.show()
print("-----After Insert Mid---------")
n1.insert(n3,"Sabari")
n1.show()
print("-----After Insert Begining---------")
n1.insert_beg("Maha")
n1.show()
print("-----After Insert End---------")
n1.insert_end("Mohan")
n1.show()
print("-----After Remove---------")
n1.remove("l,,")
n1.show()