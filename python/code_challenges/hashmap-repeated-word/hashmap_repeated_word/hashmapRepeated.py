from hashmap_repeated_word.linkedlist import *
import re

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


def repeated_word(sentence =None):
    if sentence == None :
        return 'empty sentence'
    hash_map = HashTable(720)

    sentence = re.sub('\W+', ' ', sentence).split()

    for item in sentence:

        if hash_map.contains(item):
            return item
        else:

            hash_map.add(item, True)



if __name__ == "__main__":

    sentence="iam ahmad shaher -- first name is ahmad"

    print(repeated_word(sentence))




