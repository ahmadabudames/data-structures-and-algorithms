import pytest
from linked_list.stack_and_queue import Queue, Stack, Node, StackEmptyException



@pytest.fixture
def data():
  new_stack = Stack()

  return {'stack':new_stack}



def test_stack_pushing_one_element():
    test_1=Stack()
    test_1.push(2)
    assert test_1.top.value==2


def test_push_multiple_values_onto_stack():
    test_2=Stack()
    test_2.push(3)
    test_2.push(10)
    assert test_2.top.value


def test_pop_off_the_stack():
    test_3=Stack()
    test_3.push(22)
    assert test_3.pop()


def test_empty_a_stack_after_multiple_pops():
    test_4=Stack()
    test_4.pop()
    test_4.pop()
    assert test_4.is_empty()==True

# def test_peek_the_next_item():
#     test_5=Stack()
#     actual = test_5.peek()
#     expected = 5
#     assert actual == expected

def test_empty_stack():
    test_6=Stack()
    assert test_6.is_empty()==True


def test_pop_or_peek_on_empty_stack_raises_exception():
    test_7=Stack()
    test_7.pop()
    test_7.peek()
    assert test_7.pop()=='Stack is empty'
    assert test_7.peek()=='Stack is empty'

def test_enqueue_into_a_queue():
    test_8=Queue()
    assert test_8.rear.value == 5
    assert test_8.front.value == 6


























# def test_stack_pop_one_element(data):
#     data['stack'].push(1)
#     data['stack'].push(2)
#     actual = data['stack'].pop()
#     expected = 2
#     assert expected == actual

# def test_stack_is_empty():
#   # create a stack
#   stack = Stack()
#   assert stack.is_empty()


# def test_stack_is_not_empty():
#   # create an empty stack
#   stack = Stack()
#   # push an item onto the stack
#   stack.top = Node(1)
#   # assert that the stack is not empty
#   assert not stack.is_empty()


# #@pytest.mark.skip
# def test_peek_empty_stack_raises_exception():
#   check_stack = Stack()
#   with pytest.raises(Exception):
#     check_stack.peek()
#     assert check_stack.peek()
#   # assert "Stack is Empty" == str(excinfo.value)




