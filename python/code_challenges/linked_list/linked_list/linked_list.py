class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value='null'):

        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")
    def includes(self,num):

        try:
          i=False
          current = self.head
          while current:
              if current.value==num:
                  i=True
                  break
              current=current.next
          return i
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")
    def __str__(self):

        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"({value}) -> none"
                break
            output = output + f"({value}) -> "
            current=current.next
        return output

    def append(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next

        last.next =  new_node


    def insertBefore(self ,value, new_data):

        current = self.head
        if current.value==value:
            self.insert(new_data)
        else:
          while current:

             if current.next.value==value :
                nextvalue=current.next
                current.next=Node(new_data)
                current.next.next=nextvalue
                break
             current=current.next

    def insertAfter(self, value, new_data):

        current = self.head
        while current:

            if current.value==value :
                nextvalue=current.next
                current.next=Node(new_data)
                current.next.next=nextvalue
                break
            current=current.next

    def NthFromLast(self, k):
        if k<0:
            print("no negative input")
        list_of_value=[]
        current = self.head
        while current:
            list_of_value+=[current.value]
            current = current.next
        if k == 0:
            print(list_of_value[-1])
        else:
            if k > len(list_of_value):
                print("exception")
            print(list_of_value[(k*-1)-1])

    







if __name__ == "__main__":
    linked_list = LinkedList()
    list1=linked_list
    list2=linked_list
    print(list1.__str__())
    print(list1.__str__())


