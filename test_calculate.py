from calculate import interest

def test_case1():
   assert interest(1000, 5, 2)[0] == 100.0
def test_case2():
   assert interest(2000, 10, 5)[0] == 1000.0
def test_case3():
   assert interest(5000, 25, 2)[0] == 2500.0

