import math
def cod(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    print('r=',r)
    print('theta = ',theta)
    return 0
x = int(input('enter x cord = '))
y = int(input('enter y cord = '))
cod(x,y)