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

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(4)
    linked_list.insert(6)
    linked_list.insert(8)
    linked_list.insert(10)
    linked_list.insert(12)
    linked_list.insert(14)

    print(linked_list.__str__())


