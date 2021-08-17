from trees.trees import Binary_s_tree


def test_for_fizz_buzz():
    tree = Binary_s_tree(10)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(15)
    tree.insert(21)
    tree.insert(20)
    tree.insert(200)
    assert tree.fizz_buzz() ==['Fizz', 'Buzz', 7, 8, 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Buzz']




