import sys
from pythonage.supercollider import PSuperCollider

# Test for supercollider

class TestRectangle:

    def __init__(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y):
        self.p1_x = p1_x
        self.p1_y = p1_y   
        self.p2_x = p2_x
        self.p2_y = p2_y   
        self.p3_x = p3_x
        self.p3_y = p3_y   
        self.p4_x = p4_x
        self.p4_y = p4_y

def tst(test):
    if test:
        print('pass')
        return
    print('**FAIL**')

def approx(foo, target):
    if foo < target - 0.00001:
        print('expected :' + str(target) + ' got: ' + str(foo))
        return False
    if foo > target + 0.00001:
        print('expected :' + str(target) + ' got: ' + str(foo))
        return False
    return True

def test_outside1():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(0.5, 1.1, tr), -0.5)
    tst(r)

def test_outside2():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(2.1, 1.1, tr), -0.1)
    tst(r)

def test_outside3():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(1.5, 0.8, tr), -0.2)
    tst(r)

def test_outside4():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(1.5, 3.3, tr), -0.3)
    tst(r)

def test_outside1b():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = PSuperCollider.is_point_inside_rectangle(0.5, 1.0, tr) == False
    tst(r)

def test_outside2b():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = PSuperCollider.is_point_inside_rectangle(2.1, 1.0, tr) == False
    tst(r)

def test_outside3b():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = PSuperCollider.is_point_inside_rectangle(1.5, 0.8, tr) == False
    tst(r)

def test_outside4b():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = PSuperCollider.is_point_inside_rectangle(1.5, 3.3, tr) == False
    tst(r)

def test_outside1c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(1.5+dx, 0.5, tr) == False
    tst(r)

def test_outside2c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(1.5+dx, 1.5, tr) == False
    tst(r)

def test_outside3c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(0.5-dx, 1.5, tr) == False
    tst(r)

def test_outside4c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(0.5-dx, 0.5, tr) == False
    tst(r)


def test_inside1c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(1.5-dx, 0.5, tr) == True
    tst(r)

def test_inside2c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(1.5-dx, 1.5, tr) == True
    tst(r)

def test_inside3c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(0.5+dx, 1.5, tr) == True
    tst(r)

def test_inside4c():
    dx = 0.01
    tr = TestRectangle(1,0, 2,1, 1,2, 0,1)
    r = PSuperCollider.is_point_inside_rectangle(0.5+dx, 0.5, tr) == True
    tst(r)


def test_inside1():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(1.1, 1.5, tr), 0.1)
    tst(r)

def test_inside2():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(2-0.11, 1.5, tr), 0.11)
    tst(r)

def test_inside3():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(1.5, 1.2, tr), 0.2)
    tst(r)

def test_inside4():
    tr = TestRectangle(1,1, 2,1, 2,3, 1,3)
    r = approx(PSuperCollider.how_far_is_point_inside_of_rectangle(1.5, 3-0.15, tr), 0.15)
    tst(r)

def test_outside_rect1():
    offset_x = 2.01
    offset_y = 0.0
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), -0.01)
    tst(r)

def test_outside_rect2():
    offset_x = 0.0
    offset_y = 2.011
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), -0.011)
    tst(r)

def test_outside_rect3():
    offset_x = 0.0
    offset_y = -2.011
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), -0.011)
    tst(r)

def test_outside_rect4():
    offset_x = -2.01
    offset_y = 0.0
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), -0.01)
    tst(r)

def test_inside_rect1():
    offset_x = 1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), 0.1)
    tst(r)

def test_inside_rect2():
    offset_x = 1.9
    offset_y = -1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), 0.1)
    tst(r)

def test_inside_rect3():
    offset_x = -1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), 0.1)
    tst(r)

def test_inside_rect4():
    offset_x = 1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = approx(PSuperCollider.how_far_is_rectangle_a_inside_rectangle_b(tr,tr2), 0.1)
    tst(r)




def test_outside_rect1b():
    offset_x = 2.01
    offset_y = 0.0
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == False
    tst(r)

def test_outside_rect2b():
    offset_x = 0.0
    offset_y = 2.011
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == False
    tst(r)

def test_outside_rect3b():
    offset_x = 0.0
    offset_y = -2.011
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == False
    tst(r)

def test_outside_rect4b():
    offset_x = -2.01
    offset_y = 0.0
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == False
    tst(r)



def test_inside_rect1b():
    offset_x = 1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == True
    tst(r)

def test_inside_rect2b():
    offset_x = 1.9
    offset_y = -1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == True
    tst(r)

def test_inside_rect3b():
    offset_x = -1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == True
    tst(r)

def test_inside_rect4b():
    offset_x = 1.9
    offset_y = 1.9
    tr = TestRectangle(-1,-1, 1,-1, 1,1, -1,1)
    tr2 = TestRectangle(-1+offset_x,-1+offset_y, 1+offset_x,-1+offset_y, 1+offset_x,1+offset_y, -1+offset_x,1+offset_y)
    r = PSuperCollider.has_rectangle_a_points_inside_rectangle_b(tr,tr2) == True
    tst(r)
    

if __name__ == '__main__':
    print('test_outside1')
    test_outside1()
    
    print('test_outside2')
    test_outside2()
    
    print('test_outside3')
    test_outside3()
    
    print('test_outside4')
    test_outside4()
    
    print('test_outside1b')
    test_outside1b()
    
    print('test_outside2b')
    test_outside2b()
    
    print('test_outside3b')
    test_outside3b()
    
    print('test_outside4b')
    test_outside4b()

    print('test_outside1c')
    test_outside1c()
    
    print('test_outside2c')
    test_outside2c()
    
    print('test_outside3c')
    test_outside3c()
    
    print('test_outside4c')
    test_outside4c()

    print('test_inside1c')
    test_inside1c()
    
    print('test_inside2c')
    test_inside2c()
    
    print('test_inside3c')
    test_inside3c()
    
    print('test_inside4c')
    test_inside4c()

    print('test_inside1')
    test_inside1()
    
    print('test_inside2')
    test_inside2()
    
    print('test_inside3')
    test_inside3()
    
    print('test_inside4')
    test_inside4()
    
    print('test_outside_rect1')
    test_outside_rect1()
    print('test_outside_rect2')
    test_outside_rect2()
    print('test_outside_rect3')
    test_outside_rect3()
    print('test_outside_rect4')
    test_outside_rect4()
    
    print('test_inside_rect1')
    test_inside_rect1()
    print('test_inside_rect2')
    test_inside_rect2()
    print('test_inside_rect3')
    test_inside_rect3()
    print('test_inside_rect4')
    test_inside_rect4()

    print('test_outside_rect1b')
    test_outside_rect1b()
    print('test_outside_rect2b')
    test_outside_rect2b()
    print('test_outside_rect3b')
    test_outside_rect3b()
    print('test_outside_rect4b')
    test_outside_rect4b()
    
    print('test_inside_rect1b')
    test_inside_rect1b()
    print('test_inside_rect2b')
    test_inside_rect2b()
    print('test_inside_rect3b')
    test_inside_rect3b()
    print('test_inside_rect4b')
    test_inside_rect4b()
    
    sys.stdin.readline()
    
    

