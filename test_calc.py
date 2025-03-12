import pytest
from main import add, substract, multiply, divide

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(-1,-1)==-2

def test_substract():
    assert substract(5,3)==2
    assert substract(-1,1)==-2
    assert substract(-1,-1)==0

def test_multiply():
    assert multiply(2,3)==6
    assert multiply(-1,1)==-1
    assert multiply(-1,-1)==1

def test_divide():
    assert divide(6,3)==2
    assert divide(-1,1)==-1
    assert divide(-1,-1)==1

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1,0)