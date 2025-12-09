import pytest

#scope="function" fixtures will be called before every test function executes
#scope="module"   fixtures will be called only once before test functions executes
#scope="class"    fixtures will be called only once before rhe class
#scope="session"  fixtures will be called only once for the session



# module --> class --> methods
# module -->function


@pytest.fixture
def setup(scope='function'):
    print("setup browser")


def test_one(setup):
    print("this is my test")