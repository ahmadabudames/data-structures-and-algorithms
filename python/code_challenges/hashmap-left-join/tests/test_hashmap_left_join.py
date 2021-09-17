from hashmap_left_join.hashmap import *


def test_hashmap_left_join():
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

    actual=hashmap_left_join(hash1,hash2)
    expected=[['outfit', 'grap', None], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
