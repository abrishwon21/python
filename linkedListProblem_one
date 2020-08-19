class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class SingLinkedList:
  def __init__(self):
    self.head=None
  def pushData(self,ndata,postn):
    new_node=Node(ndata)
    if(postn==1):
      new_node.next=self.head
      self.head=new_node
    elif(postn>1 and self.head.next!=None):
      temp=self.head
      counter=2
      while(counter!=postn):
        temp=temp.next
        counter=counter+1
      new_node.next=temp.next
      temp.next=new_node
    else:
      temp1=self.head
      while(temp1.next!=None):
        temp1=temp1.next
      temp1.next=new_node
      new_node.next=None

  def displayContent(self):
    tm=self.head
    while tm.next!=None:
      print(tm.data)
      tm=tm.next
    print(tm.data)
  def getNthNodeFromEnd(self,nth):
    count=1
    tempnode=self.head
    while(tempnode.next!=None):
      count+=1
      tempnode=tempnode.next
    nthNode=self.head
    #my max-index at which nth data exist is count-n+1
    for i in range(count-nth):
      nthNode = nthNode.next

    #now print the data at this particular position
    print("The data at the ",nth," position is ",nthNode.data)
      

#driver
def UseIt():
  while True:
    print("for creating the linked list type:1")
    print("for displaying all the contents:2")
    print("for getting the nth node from end type:3")
    op=int(input())
    lkedlist=SingLinkedList()
    if(op==1):
      dat=input("please enter the data to be inserted")
      postn=int(input("please enter the position at which the data should be inserted"))
      lkedlist.pushData(dat,postn)
      
    elif(op==2):
      print("the content of list is")
      lkedlist.displayContent()
    elif(op==3):
      positn=input("please enter the position")
      lkedlist.getNthNodeFromEnd(int(positn))
    else:
      print("Invalid choice")

#to get the nth node element
UseIt()
