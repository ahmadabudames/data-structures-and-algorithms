from tree_intersection.intersection import *



def test_intersection():

    firstTree = tree()
    firstTree.insert(100)
    firstTree.insert(90)
    firstTree.insert(300)
    firstTree.insert(20)
    firstTree.insert(200)


    secondTree = tree()

    secondTree.insert(100)
    secondTree.insert(200)
    secondTree.insert(160)
    secondTree.insert(300)
    secondTree.insert(30)

    actual=intersection(firstTree , secondTree)
    expected=[100, 200, 300]
    assert actual==expected



