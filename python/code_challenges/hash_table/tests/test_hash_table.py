
from hash_table.hash_table import *


def test_adding_key__value_to_your_hashtable():

    test=HashTable()
    test.add('1','mansaf')
    assert test.contains('1')== True


def test_returns_the_value_stored():

    test_2=HashTable()
    test_2.add('1','mansaf')
    assert test_2.get('1')=='mansaf'


def test_returns_null():

    test_3=HashTable()
    test_3.add('1','mansaf')
    assert test_3.get('2')== None







