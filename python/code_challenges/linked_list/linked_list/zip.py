from linked_list import LinkedList, Node



def zipLists(list1, list2):
        cur1=list1.head
        cur2=list2.head

        if cur1 == None or cur2 == None :
             if cur1:
                return list1.__str__()
             else :
                return list2.__str__()

        valuelist = []
        while cur1 or cur2:
            if(cur1):
                valuelist+=[cur1.value]
            cur1 = cur1.next
            if(cur2):
                valuelist+=[cur2.value]
            cur2 = cur2.next
        x=''
        for i in valuelist:
         x+=f'( {i} ) -> '
        x+='None'
        return x

if __name__ == "__main__":
    linked_list = LinkedList()
    list1=linked_list
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2=linked_list
    list2.append(5)
    list2.append(9)
    list2.append(4)

 
    print(zipLists(list1,list2))
