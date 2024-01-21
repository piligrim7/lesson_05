import math

def test_filter():
    assert list(filter(lambda x: (x**2<=x), (-2, -1, 0, 1, 2)))==[0, 1]
    assert list(filter(lambda x: (x>0), (-2, -1, 0, 1, 2)))==[1, 2]
    assert list(filter(lambda x: (x**2>x**3), (-2, -1, 0, 1, 2)))==[-2, -1]

def test_map():
    assert list(map(lambda x: (x**2), (-2, -1, 0, 1, 2)))==[4, 1, 0, 1, 4]
    assert list(map(lambda x: (int(x>0)), (-2, -1, 0, 1, 2)))==[0, 0, 0, 1, 1]
    assert list(map(lambda x: (x**2-x), (-2, -1, 0, 1, 2)))==[6, 2, 0, 0, 2]

def test_sorted():
    assert sorted((-2, 1, 0, -1, 2))==[-2, -1, 0, 1, 2]
    assert sorted((-2, 1, 0, -1, 2), reverse=True)==[2, 1, 0, -1, -2]
    assert sorted((-2, 1, 0, -1, 2), key=lambda x: x**2)==[0, 1, -1, -2, 2]

def test_pi():
    assert 3<math.pi<4
    assert round(math.pi, 4) == 3.1416

def test_sqrt():
    assert math.sqrt(0)==0
    assert math.sqrt(1)==1
    assert math.sqrt(100)==10

def test_pow():
    assert math.pow(0,2)==0
    assert math.pow(1,2)==1
    assert math.pow(2,2)==4
    assert math.pow(-1,2)==1
    assert math.pow(-1,3)==-1
    assert math.pow(-2,2)==4
    assert math.pow(-2,3)==-8

def test_hypot():
    assert math.hypot(3,4)==5
    assert math.hypot(3,-4)==5
    assert math.hypot(6,8)==10
    assert math.hypot(1,2)==math.sqrt(5)