#Grouping tests


import pytest

@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.skip
def test_LoginByEmail():
    print(" This is login by email test")
    assert 1==1

@pytest.mark.sanity
def test_LoginByFacebook():
    print(" This is login by facebook test")
    assert 1==1

@pytest.mark.regression
def test_LoginByPhone():
    print(" This is login by phone test")
    assert 1==1

@pytest.mark.sanity
@pytest.mark.regression
def test_signupEmail():
    print(" This is login by email test")
    assert True == True

@pytest.mark.sanity
def test_signupByFacebook():
    print(" This is login by facebook test")
    assert True == True

@pytest.mark.regression
def test_signupByPhone():
    print(" This is login by phone test")
    assert True == True

@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollar():
    print(" This is payment in dollar test")
    assert 1==1

@pytest.mark.sanity
def test_paymentinrupees():
    print(" This is payment in rupees test")
    assert 1==1


'''
1) run sanity tests
      pytest .\day17\test_grouping.py -v -s -m "sanity"

2) run regression tests
       pytest .\day17\test_grouping.py -v -s -m "regression"

3) run sanity and regression tests 
       pytest .\day17\test_grouping.py -v -s -m "sanity and regression"

4) run only sanity test which are not regression
        pytest .\day17\test_grouping.py -v -s -m "not regression"

5) run only regression test which are not sanity
        pytest .\day17\test_grouping.py -v -s -m "not sanity"
    

'''




