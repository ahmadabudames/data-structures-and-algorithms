from linked_list import __version__
from linked_list.linked_list import (LinkedList,Node)




def test_empty_linked_list():

    test_1=LinkedList()
    test_1.insert()
    actual=test_1.__str__()
    expected='(null) -> none'
    assert actual==expected


def test_insert_into_the_linked_list():

    test_2=LinkedList()
    test_2.insert(332)
    actual=test_2.head.value
    expected=332
    assert actual==expected


def test_first_node_in_the_linked_list():

    test_3=LinkedList()
    test_3.insert(332)
    test_3.insert(26)
    test_3.insert(778)
    test_3.insert(1000)
    actual=test_3.head.value
    expected=1000
    assert actual==expected


def test_multiple_nodes_into_the_linked_list():

    test_4=LinkedList()
    test_4.insert(4)
    test_4.insert(5)
    actual=test_4.__str__()
    expected='(5) -> (4) -> none'
    assert actual==expected

def test_return_true_when_finding_a_value():

    test_5=LinkedList()
    test_5.insert('ahmad')
    test_5.insert('abudames')
    actual=test_5.includes('ahmad')
    expected=True
    assert actual==expected

def test_return_false_when_does_not_exist():

    test_5=LinkedList()
    test_5.insert('ahmad')
    test_5.insert('abudames')
    actual=test_5.includes('mais')
    expected=False
    assert actual==expected


def test_all_collection_values_in_in_the_linedlist():

    test_6=LinkedList()
    test_6.insert("abudames")
    test_6.insert("ameen")
    test_6.insert("shahar")
    test_6.insert("ahmad")
    actual=test_6.__str__()
    expected='(ahmad) -> (shahar) -> (ameen) -> (abudames) -> none'
    assert actual==expected

def test_end_of_the_linked_list():
    test_append=LinkedList()
    test_append.insert(22)
    test_append.insert(4)
    test_append.append(2)
    actual=test_append.__str__()
    expected='(4) -> (22) -> (2) -> none'
    assert actual==expected


def test_multiple_nodes_to_the_end_of_a_linked_list():
    test_append=LinkedList()
    test_append.append(2)
    test_append.append(1)
    actual=test_append.__str__()
    expected='(2) -> (1) -> none'
    assert actual==expected

def test_before_middle_of_the_linked_list():
    test_before=LinkedList()
    test_before.append("ahmad")
    test_before.append("shaher")
    test_before.append("abudames")
    test_before.insertBefore("abudames","ameen")
    actual=test_before.__str__()
    expected='(ahmad) -> (shaher) -> (ameen) -> (abudames) -> none'
    assert actual==expected

def test_before_the_first_node_of_a_linked_list():
     test_before_first=LinkedList()
     test_before_first.append(2)
     test_before_first.append(3)
     test_before_first.insertBefore(2,1)
     actual=test_before_first.__str__()
     expected='(1) -> (2) -> (3) -> none'
     assert actual==expected


def test_insert_after():
     test_after=LinkedList()
     test_after.append(1)
     test_after.append(3)
     test_after.insertAfter(1,2)
     actual=test_after.__str__()
     expected='(1) -> (2) -> (3) -> none'
     assert actual==expected

def test_insert_after_the_last_node():
    test_after_last_node=LinkedList()
    test_after_last_node.append(1)
    test_after_last_node.append(2)
    test_after_last_node.insertAfter(2,3)
    actual=test_after_last_node.__str__()
    expected='(1) -> (2) -> (3) -> none'
    assert actual==expected

























