#implement stack using the linkedList
'''
first create linkedlist and push data in frontend or insert at the begining 
that will take order of 1 O(1)
we have the following operations in stack
1.push
2.pop
3.delete
4.get the current top value
5.search for specific data....etc
'''
class Node:
  def __init__(self,new_data):
    self.data=new_data
    self.next=None

#now create another class for linkedlist
class Stack:
  def __init__(self):
    self.head=None
  def push(self,ndata):
    #now push value at begginnig
    new_node=Node(ndata)
    new_node.next=self.head
    self.head=new_node
  def pop(self):
    #pop top value
    print(self.head.data)

  def display(self):
    temp=self.head
    while(temp.next!=None):
      print(temp.data)
      temp=temp.next
    print(temp.data)
  def getCurrentTop(self):
    pass
  #to perform all
  def allOp(self):
    while True:
      print("1.for push type 1")
      print("2.for pop type 2")
      print("3.for display the content type 3")
      print("4.get the current top type 4")
      op=int(input("please input your operation"))
      if op==1:
        data1=input("please enter the data")
        self.push(data1)
      elif op==2:
        self.pop()
      elif op==3:
        self.display()
      elif op==4:
        self.getCurrentTop()
      else:
        print("Invalid opearation")
#driver
st=Stack()
st.allOp()


