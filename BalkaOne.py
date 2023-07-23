from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pickle
# import Sortament

from math import pi
from math import sin
from okno_general import ui
from okno_general import Form
from okno_general import app

# Рисунок
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

_translate = QtCore.QCoreApplication.translate
Form.setWindowTitle(_translate("Form", "VXV"))
ui.tabWidget.setCurrentIndex(3)

# -----------------------------------------------------------------------------
# Вывод ошибки
def error_show(x):
    # ui.label_3.setText(_translate("Form", "Ошибка"))
    ui.textEdit_3.setTextColor(QtGui.QColor (255, 0, 0))
    ui.textEdit_3.setText('Ошибка данных')
    ui.textEdit_3.setTextColor(QtGui.QColor (0, 0, 0))
    ui.textEdit_3.append(x)
# Проверка ячеек на пустые значения и ","
def vvod(nomerwidgeta, strok, stolbec):
    yoy = []
    for i in range(1, strok+1):
        x = eval('ui.tableWidget{}.item({}-1, {}).text()'.format(nomerwidgeta, i, stolbec))
        if x != '': 
            x = x.replace(',', '.')
        else: 
            x = 0
        if '.' in str(x):
            yoy.append(round(float(x), 2))
        else:
            try:
                yoy.append(int(x))
            except:
                error_show('Введены буквы вместо цифр в таблицах')
    return yoy

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def delet_0(x):
    try:
        while x[-1] == 0: del x[-1]
        if x == []: x = [0]
    except:
        x.append(0)

# -----------------------------------------------------------------------------
def raschetOne(Lkl, Lbk, Lkp, Nv, Nvx1, Nvx2, Moment, MomX, privyazki):
    
    _translate = QtCore.QCoreApplication.translate
    # ui.label_3.setText(_translate("Form", "Отчет"))

    delet_0(Nv)
    delet_0(Moment)
     
    # Корректировка спиков по длине спика Nv
    kk = len (Nv); Nvx1 = Nvx1 [:kk]; Nvx2 = Nvx2 [:kk]
    # Moment = Moment [:kk]; MomX = MomX [:kk]
    # Корректировка спиков по длине спика Moment
    kk = len (Moment); MomX = MomX [:kk]
    # Длина балки
    L = sum(Lkl + Lbk + Lkp)
    L = round(L, 2)
    # Координаты опорных реакций
    xR1 = 0 if Lkl == 0 else sum(Lkl)
    xR1 = round(xR1, 2)
    xR2 = sum(Lkl + Lbk)
    xR2 = round(xR2, 2)
    
    ''' Подготовка списков для расчета опорных реакций R1 и R2: '''
    NvP = []
    Nvx = []

    for i in range(0, len(Nvx2)):
        if Nvx2[i] != 0:
            Nvx.append(((Nvx2[i] - Nvx1[i])/2) + Nvx1[i] - xR1)
            NvP.append(Nv[i] * (Nvx2[i] - Nvx1[i]))
        else:
            Nvx.append(Nvx1[i] - xR1)
            NvP.append(Nv[i])

    M = Moment
    xM = MomX

    '''
    Правило задание моментов при нахождении R2
    момент (+) - вращении по часовой стрелки.
    момент (-) - вращении против часовой стрелки.
    '''
    # Сумма моментов в точке приложения R1:
    R2 = []
    if xR1 == 0:
        for i in range(0, len(NvP)):
            try:
                R2.append(NvP[i] * Nvx[i] / xR2)
            except:
                error_show('Укажите длину балки')
                return
        for i in range(0, len(M)):
            R2.append(-M[i] / xR2)
    
    if xR1 > 0:
        for i in range(0, len(NvP)):
            R2.append(NvP[i] * Nvx[i] / (xR2 - xR1))
        for i in range(0, len(M)):
            R2.append(-M[i] / (xR2 - xR1))

    R2 = -round(sum(R2), 5)
    R1 = -round(sum(NvP) + R2, 5)

    listpriv = [0]
    for i in range(1, len(privyazki)):
        if privyazki[i] != privyazki[i-1]:
            listpriv.append(privyazki[i])
        else:
            continue
    privyazki = listpriv
    Ychastki = []
    for i in range(1, len(privyazki)):
        Ychastki.append([privyazki[i-1], privyazki[i]])
    
    '''Создаем списки координат и нагрузок для нахождения моментов и поперечной силы'''
    xP = []             # координаты сосредоточенных нагрузок 
    xQ = []             # координаты распределенных нагрузок
    xQ0 = []            # координаты распределенных нагрузок для отображения схемы кратные 0,1м
    LQ = []             # протяженность распределенных нагрузок
    P = []              # значения сосредоточенных нагрузок
    Q = []              # значения распределенных нагрузок

    for i in range(0, len(Nvx2)):
        if Nvx2[i] == 0:
            P.append(-Nv[i])
            xP.append(Nvx1[i])
        else:
            Q.append(Nv[i])
            x = Nvx1[i]
            y = []
            y.append(x)
            while x < Nvx2[i]:
                x = round(x + 0.01, 2)
                y.append(x)
            xQ.append(y)
            z = 0.0
            yl = []
            yl.append(z)
            while z < round(Nvx2[i] - Nvx1[i], 2):
                z = round(z + 0.01, 2)
                yl.append(z)
            LQ.append(yl)

    for i in range(0, len(Nvx2)):
        if Nvx2[i] != 0:
            x = Nvx1[i]
            y = []
            y.append(x)
            while x < Nvx2[i]:
                x = round(x + 0.1, 3)
                y.append(x)
            xQ0.append(y)

    for i in range(0, len(xQ0)):
        del xQ0[i][-1]
        xQ0[i].append(xQ[i][-1])

    xP0 = xP[:]
    P0 = P[:]

    '''Дополняем сосредоточенные нагрузки опорной реакцией R1, R2'''
    P.append(-R1)
    P.append(-R2)
    xP.append(xR1)
    xP.append(xR2)
    
    '''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
    '''Разбиваем балку по учассткам с шагом "n" '''
    XL = []
    for i in range(0, len(Ychastki)):
        sss = []
        sss.append(Ychastki[i][0])
        sss.append(round((Ychastki[i][-1] - Ychastki[i][0]) * 0.5 + Ychastki[i][0], 5))
        sss.append(Ychastki[i][-1])
        XL.append(sss)
    '''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# ==========================================================================================================

    '''Находим значения эпюры Mx и Qy в сечениях XL'''
    # Для каждого сечения XL
    if xP[-1] == L:
        del xP[-1]
        del P[-1]
    M_x = []
    # Q_x = []
    for i in range(0, len(XL)):
        mmmm = []
        # qqqq = []
        for x in range(0, len(XL[i])):
            y = 0
            # a = 0
            '''# перебираем координаты сосредоточенных нагрузок'''
            for q in range(0, len(P)):
                # берем только значению меньше XL не вулючая нагрузку в конце участка и беря ее в начале следующего участка
                if XL[i][x] > xP[q] or XL[i][0] == xP[q]:
                    # умножаем значение силы на плечо XL, складиываю при этом с предыдущим вычислением
                    y = y + P[q] * (XL[i][x] - xP[q])
                    # a = round(a + P[q], 5)
            '''# перебираем координаты для каждой распределенной нагрузки'''
            u = 0
            # b = 0
            for w in range(0, len(Q)):
                for e in range(0, len(xQ[w])):
                    # если распределенная нагрузка доходит до конца балки
                    if XL[i][x] == xQ[w][e]:
                        # умножаем значение силы на плечо XL, складиываю при этом с предыдущим вычислением
                        u = u + Q[w] * LQ[w][e] * (LQ[w][e] * 0.5)
                        # b = b + Q[w] * LQ[w][e]
                # если распределенная нагрузка НЕ доходит до конца балки
                if XL[i][x] > xQ[w][-1]:
                    # умножаем значение силы на плечо XL, складиываю при этом с предыдущим вычислением
                    u = round(u + Q[w] * LQ[w][-1] * ((XL[i][x] - xQ[w][-1]) + LQ[w][-1] * 0.5), 5)
                    # b = round(b + Q[w] * LQ[w][-1], 5)
            '''# перебираем координаты нагрузок от приложенных моментов'''
            j = 0
            for g in range(0, len(M)):
                if XL[i][x] > xM[g] or XL[i][0] == xM[g]:
                    j = j + M[g]
            '''Формируем слагаемые в значения по X'''
            mmmm.append(round(y - u - j, 8))
            # qqqq.append(round(a - b, 5))
        M_x.append(mmmm)
        # Q_x.append(qqqq)
        
        '''Конец перебора'''
    MxOne = M_x

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    return MxOne
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(app.exec_())
# -----------------------------------------------------------------------------