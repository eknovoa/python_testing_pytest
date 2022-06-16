from stack import Stack
import pytest

# fixtures alleviates need to retype code over and over again
@pytest.fixture
def stack():
    return Stack()

#@pytest.mark.smoke
# markers = smoke: smoke test       #anything to the right of the colon in mark decoration statement is considered a statement
        #regression
# put in file called pytest.ini

def test_constructor():
    s = Stack()     #created an instance of the Stack object
    assert isinstance(s, Stack)   # assert will either pass or fail   #isinstance (is variable s an instance of Stack)
    assert len(s) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack):
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.pop() is None




