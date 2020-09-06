import math as cm


def line(a=0, b=0):
    if not (a == 0):
        return -b / a
    else:
        return 'Ты придурок!'

def kvadr(a=0, b=0, c=0):
    if not (a == 0):
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            return x1, x2
        elif D == 0:
            x1 = -b / (2 * a)
            return x1
        else:
            return 'Действительных корней нет'


def cube(a=0, b=0, c=0, d=0):
    if not (a == 0) and (d == 0):
        dis = -4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 + 18 * a * b * c * d - 27 * a ** 2 * d ** 2
        if dis > 0:
            x1 = 0
            x2 = (-b + d ** 0.5) / (2 * a)
            x3 = (-b - d ** 0.5) / (2 * a)
            return x1, x2, x3
        if dis == 0:
            x2 = -b / (2 * a)
            return x2

    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    '''S = (4 * (3 * a * c - b ** 2) * (3 * a * c - b ** 2) * (3 * a * c - b ** 2) + (
                2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) * (2 * b ** 3 - 9 * a * b * c + 27 * a ** 3)) / (
                    2916 * a ** 6)'''
    S = (4 * (3 * a * c - b ** 2) ** 3 + (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) * (
            2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d)) / (2916 * a ** 6)
    y1 = 0
    y2 = 0
    if S < 0:
        if (q < 0):
            t = cm.atan(-2 * (-S ** 0.5) / q)
            if q > 0:
                t = cm.atan(-2 * (-S ** 0.5) / q) + cm.pi
            if q == 0:
                t = cm.pi / 2
            x1 = 2 * (-p / 3) ** 0.5 * cm.cos(t / 3) - b / (3 * a)
            x2 = 2 * (-p / 3) ** 0.5 * cm.cos((t + 2 * cm.pi) / 3) - b / (3 * a)
            x3 = 2 * (-p / 3) ** 0.5 * cm.cos((t + 4 * cm.pi) / 3) - b / (3 * a)
            if q == 0:
                x3 = -b / (3 * a)
            return x1, x2, x3
    if S > 0:
        if (-q / 2 + S ** 0.5) > 0:
            y1 = cm.exp(cm.log(cm.fabs(-q / 2 + S ** 0.5)) / 3)
        if (-q / 2 + S ** 0.5) < 0:
            y1 = -cm.exp(cm.log(cm.fabs(-q / 2 + S ** 0.5)) / 3)
        if (-q / 2 + S ** 0.5) == 0:
            y1 = 0
        if (-q / 2 - S ** 0.5) > 0:
            y2 = cm.exp(cm.log(cm.fabs(-q / 2 - S ** 0.5)) / 3)
        if (-q / 2 - S ** 0.5) < 0:
            y2 = -cm.exp(cm.log(cm.fabs(-q / 2 - S ** 0.5)) / 3)
        if (-q / 2 - S ** 0.5) == 0:
            y2 = 0
        Re = -(y1 + y2) / 2 - b / a / 3
        Im = (y1 - y2) * 3 ** 0.5 / 2
        x1 = y1 + y2 - b / a / 3
        x2 = complex(Re, Im)
        x3 = complex(Re, -Im)
        return x1, x2, x3
    if S == 0:
        if (q < 0):
            y1 = cm.exp(cm.log(cm.fabs(-q / 2)) / 3)
        if (q > 0):
            y1 = -cm.exp(cm.log(cm.fabs(-q / 2)) / 3)
        if q == 0:
            y1 = 0
        x1 = 2 * y1 - b / a / 3
        x2 = -y1 - b / a / 3
        x3 = -y1 - b / a / 3
        return x1, x2, x3