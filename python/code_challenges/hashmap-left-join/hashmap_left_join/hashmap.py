from hashmap_left_join.linkedList import *

class HashTable:

  def __init__(self,size=720) -> None:
      self.bucket = [None]*size
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



def hashmap_left_join(hash1,hash2):

    list=[]
    if hash1.bucket == hash1.size*[None] or hash2.bucket == hash2.size*[None] :
        return 'empty hash'
    for word in hash1.bucket:
        if word:
            list2=[]
            list2.append(word.head.value[0])
            list2.append(hash1.get(word.head.value[0]))
            list2.append(hash2.get(word.head.value[0]))
            list.append(list2)

    return list


if __name__ == "__main__":
    hash1 = HashTable()
    # """"""""""""""""""""""""""""
    # synonym Hashmap
    # """"""""""""""""""""""""""""
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')
    hash1.add('diligent', 'employed')
    hash1.add('outfit', 'grap')
    hash1.add('guide', 'usher')
    hash2 = HashTable()
    # """"""""""""""""""""""""""""
    # Aytonym Hashmap
    # """"""""""""""""""""""""""""
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')

    print(hashmap_left_join(hash1,hash2))








