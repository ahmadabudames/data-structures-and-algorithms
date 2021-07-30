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













