import sys
import math
from pythonage.translate import PTranslate
from pythonage.rotate import PRotate
from pythonage.matrix import PMatrix
from pythonage.pixelmap import PPixelMap

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

class user_stub:
    def __init__(self):
        pass
    
    def send(self, message):
        pass

def test_pixelmap():
    return PPixelMap('dontcare', 0.1, 0.2, True, user_stub())

def test1():
    tpm = test_pixelmap()
    tpm.calculate_position(PMatrix.unity())

    tst(approx(tpm.p1_x, 0))
    tst(approx(tpm.p1_y, 0))
    
    tst(approx(tpm.p2_x, 0.1))
    tst(approx(tpm.p2_y, 0))

    tst(approx(tpm.p3_x, 0.1))
    tst(approx(tpm.p3_y, 0.2))
    
    tst(approx(tpm.p4_x, 0.0))
    tst(approx(tpm.p4_y, 0.2))

def test2():
    rad = math.radians(10)
    cosr = math.cos(rad)
    sinr = math.sin(rad)

    tpm = test_pixelmap()
    rot = PRotate('dontcare',10,True,user_stub())
    rot.append(tpm)
    rot.calculate_position(PMatrix.unity())

    tst(approx(tpm.p1_x, 0))
    tst(approx(tpm.p1_y, 0))

    tst(approx(tpm.p2_x, 0.1 * cosr))
    tst(approx(tpm.p2_y, 0.1 * sinr))

    tst(approx(tpm.p3_x, 0.1 * cosr - 0.2 * sinr))
    tst(approx(tpm.p3_y, 0.1 * sinr + 0.2 * cosr))

    tst(approx(tpm.p4_x, 0 - 0.2 * sinr))
    tst(approx(tpm.p4_y, 0.2 * cosr))

def test3():
    rad = math.radians(10)
    cosr = math.cos(rad)
    sinr = math.sin(rad)

    tpm = test_pixelmap()
    rot = PRotate('dontcare',10,True,user_stub())
    rot.append(tpm)

    tx = 100
    ty = 200
    tran = PTranslate('dontcare',tx,ty, True, user_stub())
    tran.append(rot)
    tran.calculate_position(PMatrix.unity())

    tst(approx(tpm.p1_x, 0+tx))
    tst(approx(tpm.p1_y, 0+ty))

    tst(approx(tpm.p2_x, 0.1 * cosr+tx))
    tst(approx(tpm.p2_y, 0.1 * sinr+ty))

    tst(approx(tpm.p3_x, 0.1 * cosr - 0.2 * sinr+tx))
    tst(approx(tpm.p3_y, 0.1 * sinr + 0.2 * cosr+ty))

    tst(approx(tpm.p4_x, 0 - 0.2 * sinr+tx))
    tst(approx(tpm.p4_y, 0.2 * cosr+ty))

def test4():
    rad = math.radians(10)
    cosr = math.cos(rad)
    sinr = math.sin(rad)

    tpm = test_pixelmap()
    rot = PRotate('dontcare',10,True,user_stub())

    tx = 100
    ty = 200
    tran = PTranslate('dontcare',tx,ty, True, user_stub())
    tran.append(tpm)
    rot.append(tran)
    rot.calculate_position(PMatrix.unity())

    txx = cosr * 100 - 200 * sinr
    tyy = sinr * 100 + 200 * cosr

    tst(approx(tpm.p1_x, txx))
    tst(approx(tpm.p1_y, tyy))

    tst(approx(tpm.p2_x, 0.1 * cosr + txx))
    tst(approx(tpm.p2_y, 0.1 * sinr + tyy))

    tst(approx(tpm.p3_x, 0.1 * cosr - 0.2 * sinr + txx))
    tst(approx(tpm.p3_y, 0.1 * sinr + 0.2 * cosr + tyy))

    tst(approx(tpm.p4_x, 0 - 0.2 * sinr +  txx))
    tst(approx(tpm.p4_y, 0.2 * cosr +  tyy))

def test5():
    rad = math.radians(10)
    cosr = math.cos(rad)
    sinr = math.sin(rad)

    tpm = test_pixelmap()
    rot1 = PRotate('dontcare' , 10, True, user_stub())
    rot1.append(tpm)

    tx = 100
    ty = 200
    tran = PTranslate('dontcare', tx, ty, True, user_stub())
    tran.append(rot1)

    rot2 = PRotate('dontcare' , 10, True, user_stub())
    rot2.append(tran)
    rot2.calculate_position(PMatrix.unity())

    txx = cosr * 100 - 200 * sinr
    tyy = sinr * 100 + 200 * cosr

    rad2 = math.radians(20)
    cosr2 = math.cos(rad2)
    sinr2 = math.sin(rad2)

    tst(approx(tpm.p1_x, txx))
    tst(approx(tpm.p1_y, tyy))

    tst(approx(tpm.p2_x, 0.1 * cosr2 + txx))
    tst(approx(tpm.p2_y, 0.1 * sinr2 + tyy))

    tst(approx(tpm.p3_x, 0.1 * cosr2 - 0.2 * sinr2 + txx))
    tst(approx(tpm.p3_y, 0.1 * sinr2 + 0.2 * cosr2 + tyy))

    tst(approx(tpm.p4_x, 0 - 0.2 * sinr2 +  txx))
    tst(approx(tpm.p4_y, 0.2 * cosr2 +  tyy))
    

if __name__ == '__main__':

    print('test1')
    test1()
    print('test2')
    test2()
    print('test3')
    test3()
    print('test4')
    test4()
    print('test5')
    test5()

    sys.stdin.readline()
    
    

