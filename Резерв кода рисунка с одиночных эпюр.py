
    # '''Собираем значения с эпюр Мх и Qу на границах участков'''
    # granMI = []; granXI = []
    # for i in range(0, len(XL)):
    #     y = []; z = []
    #     y.append(round(M_x[i][0], 3))
    #     y.append(round(M_x[i][-1], 3))
    #     granMI.append(y)
    #     z.append(round(XL[i][0], 3))
    #     z.append(round(XL[i][-1], 3))
    #     granXI.append(z)

    # '''Находим максимальные значения  Mx и Qy по участкам балки'''
    # Mx_max_min = []
    # XL_Mx_max_min = []
    # for i in range(0, len(XL)):
    #     if max(M_x[i]) != 0 and max(M_x[i]) not in Mx_max_min:
    #         Mx_max_min.append(round(max(M_x[i]), 3))
    #         XL_Mx_max_min.append(XL[i][M_x[i].index(max(M_x[i]))])
    #     if min(M_x[i]) != 0 and min(M_x[i]) not in Mx_max_min:
    #         Mx_max_min.append(round(min(M_x[i]), 3))
    #         XL_Mx_max_min.append(XL[i][M_x[i].index(min(M_x[i]))])
    # # 
    # '''Собираем все участки в один список для построения эпюры Mx и Qy'''
    
    # M_x_ychastoki = []
    # for i in range(0, len(XL)):
    #     for x in range(0, len(XL[i])):
    #         M_x_ychastoki.append(M_x[i][x])
    #         # Q_x_ychastoki.append(Q_x[i][x])
    # M_x = M_x_ychastoki
    
    # Mmax = max(M_x)
    # Mmin = min(M_x)

    # '''Координаты сечений X перегоняем в один список для построения эпюр'''
    # XLL = []
    # for i in range(0, len(XL)):
    #     for x in range(0, len(XL[i])):
    #         XLL.append(XL[i][x])
    # XL = XLL

    # '''Собираем значения с эпюр Мх и Qу на границах участков в один список'''
    # # granQ = []
    # granM = []; granX = []
    # for i in range(0, len(XL)):
    #     for e in range(0, len(privyazki)):
    #         if XL[i] == privyazki[e]:
    #             # granQ.append(round(Q_x[i], 3))
    #             granM.append(round(M_x[i], 3))
    #             granX.append(round(XL[i], 3))
    # granX0 = granX[:]

    # '''Создаем список со значениями максимум и минимиум с каждого участка с вычетом значений на границах'''
    # MImax = []
    # xImax = []
    # mm = []; xx = []
    # for i in range(0, len(Mx_max_min)):
    #     if Mx_max_min[i] not in granM:
    #         mm.append(round(Mx_max_min[i], 3))
    #         xx.append(round(XL_Mx_max_min[i], 3))
    # MImax.append(mm)
    # xImax.append(xx)

    # '''Добавляем в список со значениями границ участков максимумы и минимиумы с каждого участка'''
    # for i in range(0, len(Mx_max_min)):
    #     if Mx_max_min[i] not in granM:
    #         # granQ.append(0.0)
    #         granM.append(round(Mx_max_min[i], 3))
    #         granX.append(round(XL_Mx_max_min[i], 3))

    # '''====================================================================================================================================='''
    # '''====================================================================================================================================='''
    # class Example(QWidget):
    #     def __init__(self):
    #         super().__init__()
    #         self.initUI()
    #     def initUI(self):
    #         self.setGeometry(0, 0, Wrisunka, Hrisunka)
    #         self.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
    #     def paintEvent(self, e):
    #         qp = QPainter()
    #         qp.begin(self)
    #         self.drawBrushes(qp)
    #         qp.end()

    #     def drawBrushes(self, qp):
    #         '''Сдвигаем координаты Х'''
    #         dx = 15

    #         ''' масштаб эпюр по горизонту '''
    #         masshtabX = (Wrisunka - 30)/L

    #         '''координата оси балки'''
    #         dy = 40
    #         if len(P0) == 0 or sum(M) == 0:
    #             nP = 0
    #         if len(P0) != 0 or sum(M) != 0:
    #             nP = 1
    #         nN = len(Q) + nP
    #         osBalki = dy * nN + 20

    #         '''Максимальное количество пикселей по вертикали на каждую эпюру
    #         с вычетом места под надписи эпюр и цифр значений:
    #         90 + 45 + 60 + 60 + 15 = 270
    #         90 - расстояние от оси балки до нижней точки размерной линии
    #         60 + 60 - расстояния между крайними точками соседних эпюр
    #         15 - расстояние от нижней точки последней эпюры до конца рисунка

    #         90 + 50 + 70 + 70 + 15 = 295
    #         90 - расстояние от оси балки до нижней точки размерной линии
    #         60 + 60 - расстояния между крайними точками соседних эпюр
    #         15 - расстояние от нижней точки последней эпюры до конца рисунка'''
    #         Yos = (Hrisunka - osBalki - 295)/3 - 0

    #         '''Согласно выделенного количество пикселей по вертикали на каждую эпюру
    #         масштабируем вертикальные значения эпюр'''
    #         try:
    #             masshtabYM = Yos/(abs(Mmax) + abs(Mmin))
    #         except:
    #             masshtabYM = 1

    #         '''Координата оси эпюры Qy'''
    #         '''osQy = abs(Qmax) * masshtabYQ + osBalki + 140'''

    #         '''Координата оси эпюры Mx'''
    #         '''osMx = osQy + abs(Qmin) * masshtabYQ + 70 + abs(Mmin) * masshtabYM'''
    #         osMx = abs(Mmax) * masshtabYM + osBalki + 200

    #         ''' Схема загружения балки '''
    #         '''Опорные шарниры'''
    #         d = 8
    #         qp.setPen(QPen(QtGui.QColor(0, 100, 150), 1.5, QtCore.Qt.SolidLine))
    #         # drawEllipse(int x, int y, int width, int height)
    #         qp.drawEllipse (xR1 * masshtabX + dx - d/2, osBalki + 5, d, d)
    #         qp.drawEllipse (xR2 * masshtabX + dx - d/2, osBalki + 5, d, d)
    #         '''Наклонные линии R1 и вертикальная R2'''
    #         qp.drawLine(xR1 * masshtabX + dx + 3, osBalki + d + 5, xR1 * masshtabX + dx + 10, osBalki + 25)
    #         qp.drawLine(xR1 * masshtabX + dx - 3, osBalki + d + 5, xR1 * masshtabX + dx - 10, osBalki + 25)
    #         qp.drawLine(xR2 * masshtabX + dx, osBalki + d + 5, xR2 * masshtabX + dx, osBalki + 25)
    #         '''Горизонтальные толстые линии R1 и R2'''
    #         qp.setPen(QPen(QtGui.QColor(0, 100, 150), 3, QtCore.Qt.SolidLine))
    #         qp.drawLine(xR1 * masshtabX, osBalki + 25, xR1 * masshtabX + dx + dx, osBalki + 25)
    #         qp.drawLine(xR2 * masshtabX + dx - 10, osBalki + 25, xR2 * masshtabX + dx + 10, osBalki + 25)
    #         '''Горизонтальные тонкие линии R1 и R2'''
    #         qp.setPen(QPen(QtGui.QColor(0, 100, 150), 1, QtCore.Qt.SolidLine))
    #         qp.drawLine(xR1 * masshtabX, osBalki + 30, xR1 * masshtabX + dx + dx, osBalki + 30)
    #         qp.drawLine(xR2 * masshtabX + dx - 10, osBalki + 30, xR2 * masshtabX + dx + 10, osBalki + 30)

    #         '''Балка'''
    #         qp.setPen(QPen(QtGui.QColor(0, 0, 0), 3, QtCore.Qt.SolidLine))
    #         qp.drawLine(XL[0] * masshtabX + dx, osBalki, XL[-1] * masshtabX + dx, osBalki)
    #         qp.setPen(QPen(QtGui.QColor(0, 100, 150), 2, QtCore.Qt.SolidLine))
            
    #         '''Расстановка R1 и R2 (стрелки и значения)'''
    #         qp.setPen(QPen(QtGui.QColor(255, 85, 0), 3, QtCore.Qt.SolidLine))
    #         qp.drawLine(xR1 * masshtabX + dx, osBalki + 35, xR1 * masshtabX + dx, osBalki + 60)
    #         qp.setFont(QtGui.QFont("Cambria", 11))
    #         qp.drawText(xR1 * masshtabX + dx + 5, osBalki + 45, 50, 30, Qt.AlignLeft, str(abs(round(R1, 3))))
    #         qp.drawText(xR2 * masshtabX + dx - 55, osBalki + 45, 50, 30, Qt.AlignRight, str(abs(round(R2, 3))))
    #         qp.setPen(QPen(QtGui.QColor(255, 85, 0), 2, QtCore.Qt.SolidLine))
    #         if R1 <= 0:
    #             qp.drawLine(xR1 * masshtabX + dx, osBalki + 35, xR1 * masshtabX + dx - 3, osBalki + 43)
    #             qp.drawLine(xR1 * masshtabX + dx, osBalki + 35, xR1 * masshtabX + dx + 3, osBalki + 43)
    #             qp.drawLine(xR1 * masshtabX + dx - 3, osBalki + 43, xR1 * masshtabX + dx + 3, osBalki + 43)
    #         else:
    #             qp.drawLine(xR1 * masshtabX + dx, osBalki + 60, xR1 * masshtabX + dx - 3, osBalki + 52)
    #             qp.drawLine(xR1 * masshtabX + dx, osBalki + 60, xR1 * masshtabX + dx + 3, osBalki + 52)
    #             qp.drawLine(xR1 * masshtabX + dx - 3, osBalki + 52, xR1 * masshtabX + dx + 3, osBalki + 52)
    #         qp.setPen(QPen(QtGui.QColor(255, 85, 0), 3, QtCore.Qt.SolidLine))
    #         qp.drawLine(xR2 * masshtabX + dx, osBalki + 35, xR2 * masshtabX + dx, osBalki + 60)
    #         qp.setPen(QPen(QtGui.QColor(255, 85, 0), 2, QtCore.Qt.SolidLine))
    #         if R2 <= 0:
    #             qp.drawLine(xR2 * masshtabX + dx, osBalki + 35, xR2 * masshtabX + dx - 3, osBalki + 43)
    #             qp.drawLine(xR2 * masshtabX + dx, osBalki + 35, xR2 * masshtabX + dx + 3, osBalki + 43)
    #             qp.drawLine(xR2 * masshtabX + dx - 3, osBalki + 43, xR2 * masshtabX + dx + 3, osBalki + 43)
    #         else:
    #             qp.drawLine(xR2 * masshtabX + dx, osBalki + 60, xR2 * masshtabX + dx - 3, osBalki + 52)
    #             qp.drawLine(xR2 * masshtabX + dx, osBalki + 60, xR2 * masshtabX + dx + 3, osBalki + 52)
    #             qp.drawLine(xR2 * masshtabX + dx - 3, osBalki + 52, xR2 * masshtabX + dx + 3, osBalki + 52)
            
    #         '''Расстановка сосредоточенных нагрузок'''
    #         yoy = 0
    #         if len(P0) != 0:
    #             for i in range(0, len(xP0)):
    #                 if P0[i] != 0:
    #                     qp.setPen(QPen(QtGui.QColor(85, 0, 255), 3, QtCore.Qt.SolidLine))
    #                     qp.drawLine(xP0[i] * masshtabX + dx, osBalki - yoy - 5, xP0[i] * masshtabX + dx, osBalki - yoy - 35)
    #                     qp.setFont(QtGui.QFont("Cambria", 11))
    #                     if xP0[i] < L - 0.5:
    #                         qp.drawText(xP0[i] * masshtabX + dx + 5, osBalki - yoy - 30, 50, 30, Qt.AlignLeft, str(abs(P0[i])))
    #                     else:
    #                         qp.drawText(xP0[i] * masshtabX + dx - 55, osBalki - yoy - 30, 50, 30, Qt.AlignRight, str(abs(P0[i])))
    #                     qp.setPen(QPen(QtGui.QColor(85, 0, 255), 2, QtCore.Qt.SolidLine))
    #                     if P0[i] <= 0:
    #                         qp.drawLine(xP0[i] * masshtabX + dx, osBalki - yoy - 5, xP0[i] * masshtabX + dx - 3, osBalki - yoy - 13)
    #                         qp.drawLine(xP0[i] * masshtabX + dx, osBalki - yoy - 5, xP0[i] * masshtabX + dx + 3, osBalki - yoy - 13)
    #                         qp.drawLine(xP0[i] * masshtabX + dx - 3, osBalki - yoy - 13, xP0[i] * masshtabX + dx + 3, osBalki - yoy - 13)
    #                     if P0[i] > 0:
    #                         qp.drawLine(xP0[i] * masshtabX + dx, osBalki - yoy - 35, xP0[i] * masshtabX + dx - 3, osBalki - yoy - 27)
    #                         qp.drawLine(xP0[i] * masshtabX + dx, osBalki - yoy - 35, xP0[i] * masshtabX + dx + 3, osBalki - yoy - 27)
    #                         qp.drawLine(xP0[i] * masshtabX + dx - 3, osBalki - yoy - 27, xP0[i] * masshtabX + dx + 3, osBalki - yoy - 27)

    #         '''Расстановка моментов'''
    #         if len(M) != 0:
    #             for i in range(0, len(M)):
    #                 if M[i] != 0:
    #                     qp.setPen(QPen(QtGui.QColor(255, 170, 0), 3, QtCore.Qt.SolidLine))
    #                     qp.setFont(QtGui.QFont("Cambria", 11))
    #                     qp.drawText(xM[i] * masshtabX + dx - 25, osBalki - yoy - 44, 50, 30, Qt.AlignHCenter, str(abs(M[i])))
    #                     qp.setPen(QPen(QtGui.QColor(255, 170, 0), 2, QtCore.Qt.SolidLine))
    #                     qp.drawLine(xM[i] * masshtabX + dx, osBalki - yoy - 20, xM[i] * masshtabX + dx, osBalki - yoy + 20)
    #                     if M[i] < 0:
    #                         qp.drawLine(xM[i] * masshtabX + dx, osBalki - yoy - 20, xM[i] * masshtabX + dx + 15, osBalki - yoy - 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx + 7, osBalki - yoy - 23, xM[i] * masshtabX + dx + 15, osBalki - yoy - 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx + 7, osBalki - yoy - 17, xM[i] * masshtabX + dx + 15, osBalki - yoy - 20)

    #                         qp.drawLine(xM[i] * masshtabX + dx, osBalki - yoy + 20, xM[i] * masshtabX + dx - 15, osBalki - yoy + 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx - 7, osBalki - yoy + 23, xM[i] * masshtabX + dx - 15, osBalki - yoy + 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx - 7, osBalki - yoy + 17, xM[i] * masshtabX + dx - 15, osBalki - yoy + 20)

    #                     if M[i] > 0:
    #                         qp.drawLine(xM[i] * masshtabX + dx, osBalki - yoy + 20, xM[i] * masshtabX + dx + 15, osBalki - yoy + 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx + 7, osBalki - yoy + 23, xM[i] * masshtabX + dx + 15, osBalki - yoy + 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx + 7, osBalki - yoy + 17, xM[i] * masshtabX + dx + 15, osBalki - yoy + 20)

    #                         qp.drawLine(xM[i] * masshtabX + dx, osBalki - yoy - 20, xM[i] * masshtabX + dx - 15, osBalki - yoy - 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx - 7, osBalki - yoy - 23, xM[i] * masshtabX + dx - 15, osBalki - yoy - 20)
    #                         qp.drawLine(xM[i] * masshtabX + dx - 7, osBalki - yoy - 17, xM[i] * masshtabX + dx - 15, osBalki - yoy - 20)

    #         if sum(P0) != 0 or sum(M) != 0:
    #             yoy = yoy + 40

    #         '''Расстановка распределенных нагрузок'''
    #         for i in range(0, len(xQ0)):
    #             if Q[i] != 0:
    #                 qp.setPen(QPen(QtGui.QColor(0, 170, 127), 1, QtCore.Qt.SolidLine))
    #                 qp.setFont(QtGui.QFont("Cambria", 11))
    #                 qp.drawText(((xQ[i][-1] - xQ[i][0])/2 + xQ[i][0]) * masshtabX + dx - 25, osBalki - yoy - 42, 50, 20, Qt.AlignHCenter, str(Q[i]))
    #                 qp.drawLine(xQ0[i][0] * masshtabX + dx, osBalki - yoy - 22, xQ0[i][-1] * masshtabX + dx, osBalki - yoy - 22)
    #                 for x in range(0, len(xQ0[i])):
    #                     qp.drawLine(xQ0[i][x] * masshtabX + dx, osBalki - yoy - 5, xQ0[i][x] * masshtabX + dx, osBalki - yoy - 22)
    #                 yoy = yoy + 40

    #         '''Расстановка размеров'''
    #         qp.setPen(QPen(QtGui.QColor(120, 120, 120), 1, QtCore.Qt.SolidLine))
    #         qp.drawLine(XL[0] * masshtabX + dx - 5, osBalki + 85, XL[-1] * masshtabX + dx + 5, osBalki + 85)
    #         for i in range(0, len(granX0)):
    #             qp.drawLine(granX0[i] * masshtabX + dx - 5, osBalki + 85 + 5, granX0[i] * masshtabX + dx + 5, osBalki + 85 - 5)
    #             qp.drawLine(granX0[i] * masshtabX + dx, osBalki + 85 + 5, granX0[i] * masshtabX + dx, osBalki + 85 - 15)
    #         for i in range(0, len(Ychastki)):
    #             qp.drawText(((Ychastki[i][1] - Ychastki[i][0])/2 + Ychastki[i][0]) * masshtabX + dx -25, osBalki + 85 - 20, 50, 30, Qt.AlignHCenter, str(round(Ychastki[i][1] - Ychastki[i][0], 3)))

    #         # -------------------------------------------------------------------------
    #         ''' Подписи эпюр Mx, Qy, f '''
    #         qp.setPen(QPen(QtGui.QColor(0, 100, 150), 2, QtCore.Qt.SolidLine))
    #         qp.setFont(QtGui.QFont("Cambria", 11))
    #         qp.drawText(dx, 15, 'Расчётная схема балки')
    #         qp.drawText(dx, osMx - abs(Mmin) * masshtabYM - 30, 'Эпюра изгибающих моментов Mx [тс ∙ м]')
            
    #         '''Прорисовка эпюр'''
    #         for i in range(1, len(XL)):
    #             ''' Ось Эпюры Mx '''
    #             qp.setPen(QPen(QtGui.QColor(0, 0, 0), 2, QtCore.Qt.SolidLine))
    #             qp.drawLine(XL[i-1] * masshtabX + dx, osMx, XL[i] * masshtabX + dx, osMx)

    #             ''' График Эпюры Mx '''
    #             qp.setPen(QPen(QtGui.QColor(0, 100, 150, 150), 2, QtCore.Qt.SolidLine))
    #             qp.drawLine(XL[i-1] * masshtabX + dx, osMx + M_x[i-1] * masshtabYM, XL[i] * masshtabX + dx, osMx + M_x[i] * masshtabYM)

    #         ''' Вертикальные линии и значения на границах участкоа '''
    #         for i in range(0, len(granX)):
    #             ''' Вертикальные линии на границах участкоа '''
    #             qp.setPen(QPen(QtGui.QColor(0, 100, 150, 150), 2, QtCore.Qt.SolidLine))
    #             qp.drawLine(granX[i] * masshtabX + dx, osMx, granX[i] * masshtabX + dx, osMx + granM[i] * masshtabYM)
    #             qp.setFont(QtGui.QFont("Cambria", 10))
    #             qp.setPen(QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine))

    #         def dataM(a, b, Align, yyy=0):
    #             qp.setFont(QtGui.QFont("Cambria", 10))
    #             qp.setPen(QPen(QtGui.QColor(0, 0, 0), 1, QtCore.Qt.SolidLine))
    #             if Align == Qt.AlignLeft: xxx = 0
    #             if Align == Qt.AlignRight: xxx = 70 
    #             if Align == Qt.AlignHCenter: xxx = 35
    #             if granMI[a][b] >= 0: yyy = yyy + 3
    #             if granMI[a][b]  < 0: yyy = - yyy - 17
    #             qp.drawText(granXI[a][b] * masshtabX + dx - xxx, osMx + granMI[a][b] * masshtabYM + yyy, 70, 30, Align, str(round(granMI[a][b], 2) if granMI[a][b] != 0 else ''))
                
    #         '''Расстановка значений границ участков эп. Мх'''
    #         dataM(0, 0, Qt.AlignLeft)
    #         dataM(-1, -1, Qt.AlignRight)
    #         for i in range(0, len(granMI)-1):
    #             if granMI[i][-1] == granMI[i+1][0]:
    #                 dataM(i, -1, Qt.AlignHCenter)
    #             else:
    #                 if granMI[i+1][0] == 0:
    #                     dataM(i, -1, Qt.AlignHCenter)
    #                 if granMI[i][-1] == 0:
    #                     dataM(i+1, 0, Qt.AlignHCenter)

    #                 if granMI[i+1][0] < 0 and granMI[i][-1] > 0:
    #                     dataM(i, -1, Qt.AlignHCenter)
    #                     dataM(i+1, 0, Qt.AlignHCenter)
    #                 if granMI[i+1][0] > 0 and granMI[i][-1] < 0:
    #                     dataM(i, -1, Qt.AlignHCenter)
    #                     dataM(i+1, 0, Qt.AlignHCenter)

    #                 if granMI[i+1][0] < 0 and granMI[i][-1] < 0:
    #                     if granMI[i][-1] < granMI[i+1][0]:
    #                         dataM(i, -1, Qt.AlignHCenter, 12)
    #                         dataM(i+1, 0, Qt.AlignHCenter, abs(abs(granMI[i][-1]) - abs(granMI[i+1][0])) * masshtabYM - 0)
    #                     if granMI[i][-1] > granMI[i+1][0]:
    #                         dataM(i, -1, Qt.AlignHCenter, abs(abs(granMI[i][-1]) - abs(granMI[i+1][0])) * masshtabYM - 0)
    #                         dataM(i+1, 0, Qt.AlignHCenter, 12)

    #                 if granMI[i+1][0] > 0 and granMI[i][-1] > 0:
    #                     if granMI[i][-1] > granMI[i+1][0]:
    #                         dataM(i, -1, Qt.AlignHCenter, 12)
    #                         dataM(i+1, 0, Qt.AlignHCenter, abs(abs(granMI[i][-1]) - abs(granMI[i+1][0])) * masshtabYM - 0)
    #                     if granMI[i][-1] < granMI[i+1][0]:
    #                         dataM(i, -1, Qt.AlignHCenter, abs(abs(granMI[i][-1]) - abs(granMI[i+1][0])) * masshtabYM - 0)
    #                         dataM(i+1, 0, Qt.AlignHCenter, 12)

    #         '''Расстановка максимальных значений между границами участков'''
    #         for a in range(0, len(MImax)):
    #             for b in range(0, len(MImax[a])):
    #                 if MImax[a][b] >= 0: yyy = 3
    #                 if MImax[a][b]  < 0: yyy = - 17
    #                 qp.drawText(xImax[a][b] * masshtabX + dx - 35, osMx + MImax[a][b] * masshtabYM + yyy, 70, 30, Qt.AlignHCenter, str(round(MImax[a][b], 2) if MImax[a][b] != 0 else ''))

    # '''====================================================================================================================================='''
    # '''====================================================================================================================================='''

    # '''Размеры рисунка'''
    # Hrisunka = ui.label_32.height()
    # Wrisunka = ui.label_32.width()

    # '''Запускаем русунок русоваться для проги'''
    # ex = Example()

    # ee = ex.grab()
    # pixmap = QPixmap(ee)
    # ui.label_32.setPixmap(pixmap)

    # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # return MxOne
    # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++