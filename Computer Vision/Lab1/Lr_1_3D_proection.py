
'''
---------------------  3D - геометричні перетворення ---------------------------
Завдання:
Синтез 3D об'єкту та його геометричне перетворення:
1. Синтез куба геометричним методом - матриця;
2. Переміщення куба до центру екрану;
3. Обертання навколо пласких координатних вісій
4. Ортогональна проекція на плаский екран - елюзія 3D об'єкту.

'''

from graphics import *
import numpy as np
import math as mt

#---------------------------------- координати паралелепіпеда ------------------------------------
xw=600; yw=600; st=300
# розташування координат у строках: дальній чотирикутник - A B I M,  ближній чотирикутник D C F E
Prlpd = np.array([ [0, 0, 0, 1],
                  [st, 0, 0, 1],
                  [st, st, 0, 1],
                  [0, st, 0, 1],
                  [0, 0, st, 1],
                  [st, 0, st, 1],
                  [st, st, st, 1],
                  [0, st, st, 1]])    # по строках
print('enter matrix')
print(Prlpd)

#--------------------------------- функция проекції на xy, z=0 -------------------------------------
def ProjectXY (Figure):
   f = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('проекция на ху')
   print(Prxy)
   return Prxy

#-------------------------------------------- зміщення ----------------------------------------------
def ShiftXYZ (Figure, l, m, n):
   f = np.array([ [1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('зміщення')
   print(Prxy)
   return Prxy

#-------------------------------------------- обертання коло х----------------------------------------
def insertX (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR),  mt.cos(TetaR), 0], [0, 0, 0, 1]])
    ft=f.T
    Prxy = Figure.dot(ft)
    print('обертання коло х')
    print(Prxy)
    return Prxy

#-------------------------------------------- аксонометрія ----------------------------------------------
def dimetri (Figure, TetaG1, TetaG2):
    TetaR1=(3/14*TetaG1)/180; TetaR2=(3/14*TetaG2)/180
    f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0], [0, 1, 0, 0],  [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0]])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    print('dimetri')
    print(Prxy2)
    return Prxy2

#-------------------------------------- функція побудови паралелепіпеда -----------------------------
def PrlpdWiz(Prxy):
    Ax = Prxy[0, 0];  Ay = Prxy[0, 1]
    Bx = Prxy[1, 0];  By = Prxy[1, 1]
    Ix = Prxy[2, 0];  Iy = Prxy[2, 1]
    Mx = Prxy[3, 0];  My = Prxy[3, 1]

    Dx = Prxy[4, 0];  Dy = Prxy[4, 1]
    Cx = Prxy[5, 0];  Cy = Prxy[5, 1]
    Fx = Prxy[6, 0];  Fy = Prxy[6, 1]
    Ex = Prxy[7, 0];  Ey = Prxy[7, 1]

    # print(Ax, Ay); print(Bx, By); print(Ix, Iy);  print(Mx, My);
    # print(Dx, Dy); print(Cx, Cy); print(Fx, Fy); print(Ex, Ey);

    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ix, Iy), Point(Mx, My))
    obj.draw(win)
    obj = Polygon(Point(Dx, Dy), Point(Cx, Cy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj.draw(win)
    obj = Polygon(Point(Mx, My), Point(Ix, Iy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    return PrlpdWiz

#-------------------------------------------- побудова паралелепіпеда -----------------------------
win = GraphWin("3-D модель паралелепіпеда, аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=0; TetaG2=-90
l=(xw/3)-st; m=(yw/3)-st; n=m
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
l=(xw/3)-st; m=(yw/3)-st; n=m
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
l=(xw/3)-st; m=(yw/3)-st; n=m
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
l=(xw/2)-st; m=(yw/2)-st; n=m
Prlpd1=ShiftXYZ (Prlpd, l, m, n)
Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
#Prlpd2=insertX (Prlpd1, TetaG1)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

#---------------------------- застосування matplotlib ------------------------------------------
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt

points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])

P = [[2.06498904e-01 , -6.30755443e-07 ,  1.07477548e-03],
 [1.61535574e-06 ,  1.18897198e-01 ,  7.85307721e-06],
 [7.08353661e-02 ,  4.48415767e-06 ,  2.05395893e-01]]
Z = np.zeros((8,3))
for i in range(8): Z[i,:] = np.dot(points[i,:],P)
Z = 10.0*Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
r = [-1,1]
X, Y = np.meshgrid(r, r)

# plot vertices
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]],
 [Z[0],Z[1],Z[5],Z[4]],
 [Z[2],Z[3],Z[7],Z[6]],
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]]]

# plot sides
ax.add_collection3d(Poly3DCollection(verts,
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()