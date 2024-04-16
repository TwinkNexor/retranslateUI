## -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitle22222222ddZBFDc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

import socket



class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(338, 124)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 381, 161))
        self.tabWidget.setMaximumSize(QSize(381, 161))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 30, 211, 31))
        self.textEdit.setStyleSheet("corner-radius: 3px")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 30, 81, 31))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 151, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 151, 16))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 30, 81, 31))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 35, 201, 21))
        # self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"font: 500 11pt \"Yu Gothic Medium\"; border: BlackWhite\n"
"")
        self.tabWidget.addTab(self.tab_2, "")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        self.label.setStyleSheet("color: white;")
        self.tabWidget.setCurrentIndex(1)
        self.setStyleSheet("""QTabWidget::pane {
    background: transparent;
    border:0    ;
}

QTabBar::tab {
    background: transparent;
    color: white;
}

QLabel { color: white}

""")
        self.pushButton.setStyleSheet("color: white; border-radius: 15px;border: 3px solid white; background-color: rgb(204, 123, 90);")
        self.pushButton_2.setStyleSheet("color: white; border-radius: 15px;border: 3px solid white; background-color: rgb(204, 123, 90);")
        QMetaObject.connectSlotsByName(self)
    # setupUi
        self.pushButton.clicked.connect(self.ifclickedb1)
        self.pushButton_2.clicked.connect(self.ifclickedb2)
        self.input = QTextEdit
    def ifclickedb1(self):
        print("Clicked!")
        b = self.input
        a = ""
        print(b)
    def ifclickedb2(self):
        print("Clicked!")
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Test", u"Test", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u0434 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow {background: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:0.994318, y2:1, stop:0 rgba(204, 123, 90, 255), stop:0.551136 rgba(197, 147, 114, 255), stop:1 rgba(191, 167, 145, 255));}"
            )
    ex = Ui_MainWindow()
    ex.setupUi()
    ex.show()
    sys.exit(app.exec())
