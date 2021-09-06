from hash_table.linked_list import LinkedList


class HashTable:

  def __init__(self,size=720) -> None:
      self.bucket=[None]* size
      self.size= size


  def add(self,key,value):
    idx = self.hash(key)

    if self.bucket[idx]== None:
      self.bucket[idx]=LinkedList()
    self.bucket[idx].add([key,value])




  def get(self,key):


    idx = self.hash(key)
    if self.bucket[idx]== None:
      return None
    else:
      current = self.bucket[idx].head
      while current:
        if current.value[0] == key:
            return current.value[1]
        current = current.next



  def contains(self,key):

    idx = self.hash(key)
    if self.bucket[idx] == None:
      return False
    else:
      current = self.bucket[idx].head
      while current:
        if current.value[0] == key:
            return True
        else:
          return False



  def hash(self,key):

    value= 0
    for letter in key:
      value+= ord(letter)
    index = value * 10 % self.size
    return index




if __name__ == "__main__":
  hash=HashTable()
  hash.add('1','I')
  hash.add('2', 'LOVE')
  hash.add('3', 'MANSAF')
  print(hash.get('1'))
  print(hash.get('2'))
  print(hash.get('3'))
  print(hash.contains('1'))
  print(hash.contains('2'))
  print(hash.contains('3'))
  print(hash.contains('4'))

