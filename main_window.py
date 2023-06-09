# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(574, 587)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open_File = QAction(MainWindow)
        self.menu_open_File.setObjectName(u"menu_open_File")
        self.actionDark_mode = QAction(MainWindow)
        self.actionDark_mode.setObjectName(u"actionDark_mode")
        self.actionLight_mode = QAction(MainWindow)
        self.actionLight_mode.setObjectName(u"actionLight_mode")
        self.actionSolve_game = QAction(MainWindow)
        self.actionSolve_game.setObjectName(u"actionSolve_game")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.action_Help = QAction(MainWindow)
        self.action_Help.setObjectName(u"action_Help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 561, 531))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 574, 22))
        self.menuNew_Game = QMenu(self.menubar)
        self.menuNew_Game.setObjectName(u"menuNew_Game")
        self.menuColor_scheme = QMenu(self.menuNew_Game)
        self.menuColor_scheme.setObjectName(u"menuColor_scheme")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNew_Game.menuAction())
        self.menuNew_Game.addAction(self.menu_new)
        self.menuNew_Game.addAction(self.menu_open_File)
        self.menuNew_Game.addAction(self.menuColor_scheme.menuAction())
        self.menuNew_Game.addAction(self.actionAbout)
        self.menuNew_Game.addAction(self.action_Help)
        self.menuNew_Game.addAction(self.actionExit)
        self.menuNew_Game.addSeparator()
        self.menuNew_Game.addAction(self.actionSolve_game)
        self.menuColor_scheme.addAction(self.actionDark_mode)
        self.menuColor_scheme.addAction(self.actionLight_mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SudoKu", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New ...", None))
        self.menu_open_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionDark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.actionLight_mode.setText(QCoreApplication.translate("MainWindow", u"Light mode", None))
        self.actionSolve_game.setText(QCoreApplication.translate("MainWindow", u"Solve game", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuNew_Game.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuColor_scheme.setTitle(QCoreApplication.translate("MainWindow", u"Color scheme", None))
    # retranslateUi

