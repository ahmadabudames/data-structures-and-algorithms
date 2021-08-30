from marge_sort.margeSort import *


def test_marge_sort():
    test=marge_sort
    list=[4,23,55,77,10,200]
    assert test(list,0,5)==[4, 10, 23, 55, 77, 200]

