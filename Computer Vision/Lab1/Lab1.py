'''
---------------------  2D - геометричні перетворення ---------------------------
Завдання:
Програма повинна будувати 2D графічний об’єкт та реалізовувати його перетворення:
1. Переміщення, як тиражування зображення та в режимі анімації;
2. Обертання, як тиражування зображення та в режимі анімації;
3. Перетворення реалізувати в скалярній та матричній формах.

'''



import math as mt

import numpy as np

from graphics import *

#--------------------------- координати паралелепіпеда ------------------------------
xw=600; yw=600; st=300
# розташування координат у строках: дальній чотирикутник - A B I M,  ближній чотирикутник D C F E
Prlpd = np.array([ [0, 0, 0, 1],
                  [st, 0, 0, 1],
                  [st, st, 0, 1],
                  [0, st, 0, 1],
                  [0, 0, st, 1],
                  [st, 0, st, 1],
                  [st, st, st, 1],
                  [0, st, st, 1]]  )    # по строках
print('enter matrix')
print(Prlpd)
#------------------- функция проекції на xy, z=0 ---------------------------------
def ProjectXY (Figure):
   f = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('проекция на ху')
   print(Prxy)
   return Prxy
#--------------------------------- зміщення --------------------------------------
def ShiftXYZ (Figure, l, m, n):
   f = np.array([ [1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('зміщення')
   print(Prxy)
   return Prxy
#--------------------------- обертання коло х----------------------------------------
def insertX (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR),  mt.cos(TetaR), 0], [0, 0, 0, 1] ])
    ft=f.T
 e, TetaG1, TetaG2):
        TetaR1=(3/14*TetaG1)/180; TetaR2=(3/14*TetaG2)/180;
        f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0], [0, 1, 0, 0],  [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0],])
        ft1 = f1.T
        Prxy1 = Figure.dot(ft1)
        f2 = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0], [0, 0, 0, 1] ])
        ft2=f2.T
        Prxy2 = Prxy1.dot(ft2)
        print('dimetri')
        print(Prxy2)
        return Prxy2
#--------------------- функція побудови паралелепіпеда -----------------------------
def PrlpdWiz(Prxy):
    Ax = Prxy[0, 0];  Ay = Prxy[0, 1];
    Bx = Prxy[1, 0];  By = Prxy[1, 1];
    Ix = Prxy[2, 0];  Iy = Prxy[2, 1];
    Mx = Prxy[3, 0];  My = Prxy[3, 1];

    Dx = Prxy[4, 0];  Dy = Prxy[4, 1];
    Cx = Prxy[5, 0];  Cy = Prxy[5, 1];
    Fx = Prxy[6, 0];  Fy = Prxy[6, 1];
    Ex = Prxy[7, 0];  Ey = Prxy[7, 1];

    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ix, Iy), Point(Mx, My))
    obj.draw(win)
    obj = Polygon(Point(Dx, Dy), Point(Cx, Cy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj.draw(win)
    obj = Polygon(Point(Mx, My), Point(Ix, Iy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    return PrlpdWiz
#---------------------------- побудова паралелепіпеда -----------------------------
win = GraphWin("3-D модель паралелепіпеда, аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=0; TetaG2=-90
l=(xw/3)-st; m=(yw/3)-st; n=m;
#Prlpd1=ShiftXYZ (Prlpd, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
#Prlpd2=insertX (Prlpd1, TetaG1)
#Prxy3=ProjectXY (Prlpd2)
Prxy3=Prlpd
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда, аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=0; TetaG2=-90
l=(xw/3)-st; m=(yw/3)-st; n=m;
Prlpd1=ShiftXYZ (Prlpd, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
Prlpd2=insertX (Prlpd1, TetaG1)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда оберт коло Х аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=180; TetaG2=-90
l=(xw/3)-st; m=(yw/3)-st; n=m;
Prlpd1=ShiftXYZ (Prlpd, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
Prlpd2=insertX (Prlpd1, TetaG1)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D паралелепіпеда діметричний оберт навколо Х та У аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=180; TetaG2=-90
l=(xw/2)-st; m=(yw/2)-st; n=m;
Prlpd1=ShiftXYZ (Prlpd, l, m, n)
Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
#Prlpd2=insertX (Prlpd1, TetaG1)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

