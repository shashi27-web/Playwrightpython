'''

pre-requisite : install pytest-order plugin

pi install pytest-order

'''

import pytest

#Approch1: order test by positions

# @pytest.mark.order(2)
# def test_Login():
#     print(" this is login test")
#
# @pytest.mark.order(3)
# def test_add_item():
#     print(" this is add item test")
#
# @pytest.mark.order(1)
# def test_logout():
#     print("this is logout")

#Approach 2: using before ,after

# @pytest.mark.order(1)
# def test_Login():
#     print(" this is login test")
#
# @pytest.mark.order(before="test_checkout")
# def test_add_item():
#     print(" this is add item test")
#
# @pytest.mark.order(after="test_add_item")
# def test_checkout():
#     print("this is checkout")

#Approach 3: using marker string(user defined)

@pytest.mark.order("second")
def test_add_item():
    print(" this is add item test")

@pytest.mark.order("third")
def test_checkout():
    print("this is checkout")

@pytest.mark.order("first")
def test_Login():
    print(" this is login test")