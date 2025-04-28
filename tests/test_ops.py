from src.math_ops import add,sub

def test_add():
    assert add(5,0)==5
    assert add(-1,2)==1
    
def test_sub():
    assert sub(2,3)==-1
    assert sub(5,1)==4 