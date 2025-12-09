#Fixtures: Re-usable function

import  pytest

@pytest.fixture
def setup():
    print("setup browser.....")


def test_one(setup):
    print("this is my test")

def test_two(setup):
    print("this is my test")

def test_three():
    print("this is my test")