from app import add, subtract

def test_add():
  assert add(2,3) == 5
def test_subtract():
  assert subtract(5,3) == 2
def test_purposefully_incorrect_test_add():
  assert add(1,1) == 3
  
