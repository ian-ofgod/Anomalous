# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anomalusGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = QtWidgets.QWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(20, 70, 511, 471))
        self.graphWidget.setObjectName("graphWidget")
        self.timeSlider = QtWidgets.QSlider(self.graphWidget)
        self.timeSlider.setGeometry(QtCore.QRect(0, 450, 511, 16))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.graphWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 511, 441))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.anomaliesWidget = QtWidgets.QWidget(self.centralwidget)
        self.anomaliesWidget.setGeometry(QtCore.QRect(560, 150, 191, 391))
        self.anomaliesWidget.setObjectName("anomaliesWidget")
        self.BButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.BButton.setEnabled(False)
        self.BButton.setGeometry(QtCore.QRect(30, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.BButton.setFont(font)
        self.BButton.setObjectName("BButton")
        self.plusButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.plusButton.setEnabled(False)
        self.plusButton.setGeometry(QtCore.QRect(30, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.SButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.SButton.setEnabled(False)
        self.SButton.setGeometry(QtCore.QRect(30, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.SButton.setFont(font)
        self.SButton.setObjectName("SButton")
        self.nButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.nButton.setEnabled(False)
        self.nButton.setGeometry(QtCore.QRect(120, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.nButton.setFont(font)
        self.nButton.setObjectName("nButton")
        self.RButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.RButton.setEnabled(False)
        self.RButton.setGeometry(QtCore.QRect(120, 240, 51, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.RButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.RButton.setFont(font)
        self.RButton.setObjectName("RButton")
        self.QButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.QButton.setEnabled(False)
        self.QButton.setGeometry(QtCore.QRect(120, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.QButton.setFont(font)
        self.QButton.setObjectName("QButton")
        self.FButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.FButton.setEnabled(False)
        self.FButton.setGeometry(QtCore.QRect(30, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.FButton.setFont(font)
        self.FButton.setObjectName("FButton")
        self.jButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.jButton.setEnabled(False)
        self.jButton.setGeometry(QtCore.QRect(120, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.jButton.setFont(font)
        self.jButton.setObjectName("jButton")
        self.VButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.VButton.setEnabled(False)
        self.VButton.setGeometry(QtCore.QRect(30, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.VButton.setFont(font)
        self.VButton.setObjectName("VButton")
        self.AButton = QtWidgets.QPushButton(self.anomaliesWidget)
        self.AButton.setEnabled(False)
        self.AButton.setGeometry(QtCore.QRect(120, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.AButton.setFont(font)
        self.AButton.setObjectName("AButton")
        self.anomLabel = QtWidgets.QLabel(self.anomaliesWidget)
        self.anomLabel.setEnabled(True)
        self.anomLabel.setGeometry(QtCore.QRect(0, 10, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.anomLabel.setFont(font)
        self.anomLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.anomLabel.setAutoFillBackground(False)
        self.anomLabel.setTextFormat(QtCore.Qt.PlainText)
        self.anomLabel.setScaledContents(False)
        self.anomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.anomLabel.setObjectName("anomLabel")
        self.tachyRadio = QtWidgets.QRadioButton(self.anomaliesWidget)
        self.tachyRadio.setEnabled(False)
        self.tachyRadio.setGeometry(QtCore.QRect(10, 360, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.tachyRadio.setFont(font)
        self.tachyRadio.setObjectName("tachyRadio")
        self.bradyRadio = QtWidgets.QRadioButton(self.anomaliesWidget)
        self.bradyRadio.setEnabled(False)
        self.bradyRadio.setGeometry(QtCore.QRect(100, 360, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.bradyRadio.setFont(font)
        self.bradyRadio.setObjectName("bradyRadio")
        self.optionsWidget = QtWidgets.QWidget(self.centralwidget)
        self.optionsWidget.setGeometry(QtCore.QRect(20, 20, 511, 31))
        self.optionsWidget.setObjectName("optionsWidget")
        self.inputButton = QtWidgets.QPushButton(self.optionsWidget)
        self.inputButton.setGeometry(QtCore.QRect(340, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.inputButton.setFont(font)
        self.inputButton.setMouseTracking(True)
        self.inputButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.inputButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputButton.setObjectName("inputButton")
        self.analysisButton = QtWidgets.QPushButton(self.optionsWidget)
        self.analysisButton.setEnabled(False)
        self.analysisButton.setGeometry(QtCore.QRect(0, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.analysisButton.setFont(font)
        self.analysisButton.setMouseTracking(True)
        self.analysisButton.setObjectName("analysisButton")
        self.valuesWidget = QtWidgets.QWidget(self.centralwidget)
        self.valuesWidget.setGeometry(QtCore.QRect(570, 20, 181, 121))
        self.valuesWidget.setObjectName("valuesWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.valuesWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 181, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.maxBPMDial = QtWidgets.QDial(self.gridLayoutWidget)
        self.maxBPMDial.setEnabled(False)
        self.maxBPMDial.setObjectName("maxBPMDial")
        self.gridLayout.addWidget(self.maxBPMDial, 1, 1, 1, 1)
        self.signalQualityDial = QtWidgets.QDial(self.gridLayoutWidget)
        self.signalQualityDial.setEnabled(False)
        self.signalQualityDial.setObjectName("signalQualityDial")
        self.gridLayout.addWidget(self.signalQualityDial, 0, 1, 1, 1)
        self.sQLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.sQLabel.setFont(font)
        self.sQLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sQLabel.setObjectName("sQLabel")
        self.gridLayout.addWidget(self.sQLabel, 0, 0, 1, 1)
        self.maxBPMLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.maxBPMLabel.setFont(font)
        self.maxBPMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.maxBPMLabel.setObjectName("maxBPMLabel")
        self.gridLayout.addWidget(self.maxBPMLabel, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BButton.setText(_translate("MainWindow", "B"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.SButton.setText(_translate("MainWindow", "S"))
        self.nButton.setText(_translate("MainWindow", "n"))
        self.RButton.setText(_translate("MainWindow", "R"))
        self.QButton.setText(_translate("MainWindow", "Q"))
        self.FButton.setText(_translate("MainWindow", "F"))
        self.jButton.setText(_translate("MainWindow", "j"))
        self.VButton.setText(_translate("MainWindow", "V"))
        self.AButton.setText(_translate("MainWindow", "A"))
        self.anomLabel.setText(_translate("MainWindow", "DETECTED ANOMALIES"))
        self.tachyRadio.setText(_translate("MainWindow", "TACHYCARDIA"))
        self.bradyRadio.setText(_translate("MainWindow", "BRADYCARDIA"))
        self.inputButton.setText(_translate("MainWindow", "INPUT"))
        self.analysisButton.setText(_translate("MainWindow", "ANALYSIS"))
        self.sQLabel.setText(_translate("MainWindow", "SIGNAL QUALITY"))
        self.maxBPMLabel.setText(_translate("MainWindow", "MAX BPM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())