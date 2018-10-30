# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(598, 416)
        MainWidget.setStyleSheet("background-color: #26272a;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(MainWidget)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    text-algn:right;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(MainWidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/findMusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/FM.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/friends.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(MainWidget)
        self.label_4.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    text-algn:right;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/localMusic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(MainWidget)
        self.label_5.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    text-algn:right;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_7 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"color:#c3c3c3;\n"
"border:0px;\n"
"\n"
"background-color:#26272a;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border:0px;\n"
"\n"
"background-color:#404246;\n"
"text-align: left;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/likes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_10 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border-image: url(:/images/music_img.png);\n"
"border:0px;\n"
"width:60px;\n"
"height:60px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/images/music_img.png);\n"
"image: url(:/UI/images/resize_l.png);\n"
"border:0px;\n"
"width:60px;\n"
"height:60px;\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(MainWidget)
        self.label_6.setStyleSheet("QLabel{\n"
"    color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(30, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"width:24px;\n"
"height:24px;\n"
"border-image: url(:/images/like_normal.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"border:0px;\n"
"width:24px;\n"
"height:24px;\n"
"border-image: url(/images/like_hover.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:pressed{\n"
"border:0px;\n"
"width:24px;\n"
"height:24px;\n"
"border-image: url(/images/like_pressed.png);\n"
"background-color:transparent;\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(MainWidget)
        self.label_7.setStyleSheet("QLabel{\n"
"    color:#c3c3c3;\n"
"\n"
"}")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 2)
        self.pushButton_9 = QtWidgets.QPushButton(MainWidget)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"width:24px;\n"
"height:24px;\n"
"border-image: url(:/images/share_normal.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"border:0px;\n"
"width:24px;\n"
"height:24px;\n"
"border-image: url(:/images/share_hover.png);\n"
"background-color:transparent;\n"
"}\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.graphicsView = QtWidgets.QGraphicsView(MainWidget)
        self.graphicsView.setStyleSheet("QGraphicsView{\n"
"border:0px;\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 150)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pause_3 = QtWidgets.QPushButton(MainWidget)
        self.pause_3.setAutoFillBackground(False)
        self.pause_3.setStyleSheet("QPushButton{\n"
"    color:#c3c3c3;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/lastOne_normal.png);\n"
"    background-color:transparent;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/lastOne_hover.png);\n"
"    background-color:transparent;\n"
"\n"
"}")
        self.pause_3.setText("")
        self.pause_3.setIconSize(QtCore.QSize(32, 32))
        self.pause_3.setAutoExclusive(False)
        self.pause_3.setFlat(False)
        self.pause_3.setObjectName("pause_3")
        self.horizontalLayout.addWidget(self.pause_3)
        self.pause = QtWidgets.QPushButton(MainWidget)
        self.pause.setAutoFillBackground(False)
        self.pause.setStyleSheet("QPushButton{\n"
"    color:#c3c3c3;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/play_normal.png);\n"
"    background-color:transparent;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/play_hover.png);\n"
"    background-color:transparent;\n"
"\n"
"}")
        self.pause.setText("")
        self.pause.setAutoExclusive(False)
        self.pause.setFlat(False)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.pause_2 = QtWidgets.QPushButton(MainWidget)
        self.pause_2.setAutoFillBackground(False)
        self.pause_2.setStyleSheet("QPushButton{\n"
"    color:#c3c3c3;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/nextOne_normal.png);\n"
"    background-color:transparent;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/nextOne_hover.png);\n"
"    background-color:transparent;\n"
"\n"
"}")
        self.pause_2.setText("")
        self.pause_2.setIconSize(QtCore.QSize(32, 32))
        self.pause_2.setAutoExclusive(False)
        self.pause_2.setFlat(False)
        self.pause_2.setObjectName("pause_2")
        self.horizontalLayout.addWidget(self.pause_2)
        self.label = QtWidgets.QLabel(MainWidget)
        self.label.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    width:32px;\n"
"    height:32px;\n"
"    text-algn:right;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider_2 = QtWidgets.QSlider(MainWidget)
        self.horizontalSlider_2.setStyleSheet("QSlider{\n"
"    width:400px;\n"
"    height:32px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #4A708B;\n"
"background: #C0C0C0;\n"
"height: 4px;\n"
"border-radius: 1px;\n"
"padding-left:-1px;\n"
"padding-right:-1px;\n"
"} \n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #e4231f, stop: 1 #e4231f);\n"
"border: 1px solid #4A708B;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.2, fx:0.5, fy:0.5, \n"
"    stop:0.6 red, stop:0.778409 rgba(255, 255, 255, 255));\n"
"    width: 16px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 8px;\n"
"} \n"
"QSlider::add-page:horizontal {\n"
"background: #343436;\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.6 red, \n"
"    stop:0.778409 rgba(255, 255, 255, 255));\n"
" \n"
"    width: 16px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 8px;\n"
"}\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #00009C;\n"
"border-color: #999;\n"
"}\n"
" \n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider_2.setProperty("value", 20)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout.addWidget(self.horizontalSlider_2)
        self.label_2 = QtWidgets.QLabel(MainWidget)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    width:32px;\n"
"    height:32px;\n"
"    text-algn:right;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(MainWidget)
        self.horizontalSlider_3.setEnabled(True)
        self.horizontalSlider_3.setStyleSheet("QSlider{\n"
"    width:100px;\n"
"    height:32px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #4A708B;\n"
"background: #C0C0C0;\n"
"height: 4px;\n"
"border-radius: 1px;\n"
"padding-left:-1px;\n"
"padding-right:-1px;\n"
"} \n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #e4231f, stop: 1 #e4231f);\n"
"border: 1px solid #4A708B;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.2, fx:0.5, fy:0.5, \n"
"    stop:0.6 red, stop:0.778409 rgba(255, 255, 255, 255));\n"
"    width: 16px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 8px;\n"
"} \n"
"QSlider::add-page:horizontal {\n"
"background: #343436;\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.3, fx:0.5, fy:0.5, stop:0.6 red, \n"
"    stop:0.778409 rgba(255, 255, 255, 255));\n"
" \n"
"    width: 16px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 8px;\n"
"}\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #00009C;\n"
"border-color: #999;\n"
"}\n"
" \n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider_3.setProperty("value", 20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout.addWidget(self.horizontalSlider_3)
        self.pause_4 = QtWidgets.QPushButton(MainWidget)
        self.pause_4.setStyleSheet("QPushButton{\n"
"    color:#c3c3c3;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/lyric_normal.png);\n"
"    background-color:transparent;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border:0px;\n"
"    width:32px;\n"
"    height:32px;\n"
"    border-image: url(:/images/lyric_hover.png);\n"
"    background-color:transparent;\n"
"\n"
"}")
        self.pause_4.setText("")
        self.pause_4.setObjectName("pause_4")
        self.horizontalLayout.addWidget(self.pause_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "MainWidget"))
        self.label_3.setText(_translate("MainWidget", "推荐"))
        self.pushButton.setText(_translate("MainWidget", "发现音乐"))
        self.pushButton_2.setText(_translate("MainWidget", "私人FM"))
        self.pushButton_3.setText(_translate("MainWidget", "视频"))
        self.pushButton_4.setText(_translate("MainWidget", "朋友"))
        self.label_4.setText(_translate("MainWidget", "我的音乐"))
        self.pushButton_5.setText(_translate("MainWidget", "本地音乐"))
        self.pushButton_6.setText(_translate("MainWidget", "下载管理"))
        self.label_5.setText(_translate("MainWidget", "创建的歌单"))
        self.pushButton_7.setText(_translate("MainWidget", "我喜欢的音乐"))
        self.label_6.setText(_translate("MainWidget", "演员"))
        self.label_7.setText(_translate("MainWidget", "薛之谦"))
        self.label.setText(_translate("MainWidget", "04:30"))
        self.label_2.setText(_translate("MainWidget", "04:30"))

import ui_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())

