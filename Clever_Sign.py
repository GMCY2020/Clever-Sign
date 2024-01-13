# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_46554689
# Created by: GMCY
# 2021/3/13

from os import listdir, system
from numpy import argmin
from sys import argv, exit
from threading import Thread
from time import localtime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from cv2 import imwrite, VideoCapture, resize, rectangle, putText, FONT_HERSHEY_DUPLEX, FILLED
from face_recognition import load_image_file, face_locations, face_encodings, compare_faces, face_distance


def history_write(String):
    times = localtime()
    daytime = str(times[0]) + '-' + str(times[1]) + '-' + str(times[2]) + '\t' + str(times[3]) + ':' + str(
        times[4]) + ':' + str(times[5]) + '\t'
    with open('History.txt', 'a', encoding='utf-8') as f:
        f.write(daytime + str(String) + '\n')


def history():
    thread = Thread(
        target=system,
        args=('History.txt',)
    )
    thread.start()


class UiSignWindow(object):
    def __init__(self):
        self.label_image = None
        self.verticalLayout_2 = None
        self.widget_command = None
        self.horizontalLayout_2 = None
        self.lineEdit_command = None
        self.known_face_names = None
        self.dialog = None
        self.names = None
        self.frame = None
        self.lineEdit = None
        self.face_names = None
        self.my_face_locations = None
        self.widget_show = None
        self.label_command = None
        self.pushButton_stop = None
        self.pushButton_start = None
        self.known_face_encodings = None
        self.pushButton_local = None
        self.widget_under = None
        self.pushButton_history = None
        self.widget_top = None
        self.verticalLayout_3 = None
        self.widget_set = None
        self.horizontalLayout = None
        self.centralWidget = None
        self.error_start = 0
        self.error_local = 0
        self.error_known = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SignWindow")
        MainWindow.resize(500, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget.setObjectName("central-widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_set = QtWidgets.QWidget(self.centralWidget)
        self.widget_set.setMinimumSize(QtCore.QSize(150, 580))
        self.widget_set.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_set.setMouseTracking(False)
        self.widget_set.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.widget_set.setObjectName("widget_set")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_set)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_top = QtWidgets.QWidget(self.widget_set)
        self.widget_top.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_top.setObjectName("widget_top")
        self.pushButton_history = QtWidgets.QPushButton(self.widget_top)
        self.pushButton_history.setGeometry(QtCore.QRect(10, 10, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.pushButton_history.setObjectName("pushButton_history")
        self.verticalLayout_3.addWidget(self.widget_top)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.widget_under = QtWidgets.QWidget(self.widget_set)
        self.widget_under.setMinimumSize(QtCore.QSize(0, 163))
        self.widget_under.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget_under.setObjectName("widget_under")
        self.pushButton_local = QtWidgets.QPushButton(self.widget_under)
        self.pushButton_local.setGeometry(QtCore.QRect(10, 120, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_local.setFont(font)
        self.pushButton_local.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_local.setObjectName("pushButton_local")
        self.pushButton_start = QtWidgets.QPushButton(self.widget_under)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 10, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.widget_under)
        self.pushButton_stop.setGeometry(QtCore.QRect(10, 60, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_3.addWidget(self.widget_under)
        self.horizontalLayout.addWidget(self.widget_set)
        self.widget_show = QtWidgets.QWidget(self.centralWidget)
        self.widget_show.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_show.setStyleSheet("")
        self.widget_show.setObjectName("widget_show")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_show)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_image = QtWidgets.QLabel(self.widget_show)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setStyleSheet("")
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_image.setScaledContents(True)
        pixmap = QPixmap('bg.jpg')
        self.label_image.setPixmap(pixmap)
        self.verticalLayout_2.addWidget(self.label_image)
        self.widget_command = QtWidgets.QWidget(self.widget_show)
        self.widget_command.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_command.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_command.setObjectName("widget_command")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_command)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_command = QtWidgets.QLabel(self.widget_command)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_command.setFont(font)
        self.label_command.setObjectName("label_command")
        self.horizontalLayout_2.addWidget(self.label_command)
        self.lineEdit_command = QtWidgets.QLineEdit(self.widget_command)
        self.lineEdit_command.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_command.setFont(font)
        self.lineEdit_command.setText("")
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.horizontalLayout_2.addWidget(self.lineEdit_command)
        self.verticalLayout_2.addWidget(self.widget_command)
        self.horizontalLayout.addWidget(self.widget_show)
        MainWindow.setCentralWidget(self.centralWidget)

        self.reTranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reTranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SignWindow", "人脸打卡助手"))
        self.pushButton_history.setText(_translate("MainWindow", "记录"))
        self.pushButton_local.setText(_translate("MainWindow", "录入"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止"))
        self.label_command.setText(_translate("MainWindow", "记录："))

        self.pushButton()

    def pushButton(self):
        self.pushButton_history.clicked.connect(history)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_local.clicked.connect(self.local)

        self.show_images_thread()

    def start(self):
        if self.error_start == 0:
            self.names = []
            # self.learn_images()
            self.error_start = 1
            self.pushButton_local.setStyleSheet("background-color: rgb(255, 85, 0);")

            self.lineEdit_command.setText('开始打卡')
            history_write('开始打卡')

    def stop(self):
        if self.error_start == 1:
            self.error_start = 0
            self.pushButton_local.setStyleSheet("background-color: rgb(85, 255, 127);")

            self.lineEdit_command.setText('结束打卡')
            history_write('结束打卡')

    def local(self):
        if self.pushButton_local.styleSheet() != "background-color: rgb(255, 85, 0);":
            self.show_Dialog()

    def show_Dialog(self):
        self.error_local = 1

        self.dialog = QDialog()
        self.dialog.setWindowTitle("保存头像")
        self.dialog.resize(304, 155)
        self.dialog.setMinimumSize(QtCore.QSize(304, 155))
        self.dialog.setMaximumSize(QtCore.QSize(304, 155))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 261, 41))
        self.lineEdit.setText("输入英文名")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        pushButton_yes = QtWidgets.QPushButton(self.dialog)
        pushButton_yes.setGeometry(QtCore.QRect(20, 90, 111, 41))
        pushButton_yes.setText("确认")
        pushButton_yes.setFont(font)
        pushButton_yes.setStyleSheet("background-color: rgb(85, 255, 127);")
        pushButton_yes.setObjectName("pushButton_yes")
        pushButton_yes.clicked.connect(self.save_image)

        pushButton_no = QtWidgets.QPushButton(self.dialog)
        pushButton_no.setGeometry(QtCore.QRect(170, 90, 111, 41))
        pushButton_no.setText("取消")
        pushButton_no.setFont(font)
        pushButton_no.setStyleSheet("background-color: rgb(255, 85, 0);")
        pushButton_no.setObjectName("pushButton_no")
        pushButton_no.clicked.connect(self.dialog.close)

        self.dialog.exec()
        self.error_local = 0

    def save_image(self):
        name = self.lineEdit.text()
        imwrite('img\\' + name + '.jpg', self.frame)
        self.dialog.close()
        self.lineEdit_command.setText(name + '保存成功')
        history_write(name + '保存成功')
        self.error_local = 0
        self.learn_images()

    def show_images(self):
        video_capture = VideoCapture(0)

        self.learn_images()

        self.lineEdit_command.setText('摄像头已打开')
        history_write('摄像头已打开')

        self.my_face_locations = []
        self.face_names = []

        num = 0

        while video_capture.isOpened():
            if self.error_local == 0:
                ret, self.frame = video_capture.read()

                if not ret:
                    break

            if self.error_start == 1 and num == 0 and self.error_known == 0:
                thread = Thread(
                    target=self.know_images
                )
                thread.start()

            num += 1

            if num == 15:
                num = 0

            if self.error_start == 1:
                for (top, right, bottom, left), name in zip(self.my_face_locations, self.face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), FILLED)
                    font = FONT_HERSHEY_DUPLEX
                    putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            imwrite('show.jpg', self.frame)
            pixmap = QPixmap('show.jpg')
            self.label_image.setPixmap(pixmap)

        video_capture.release()
        history_write('摄像头关闭')

    def show_images_thread(self):
        thread = Thread(target=self.show_images)
        thread.start()

    def learn_images(self):
        self.known_face_encodings = []
        self.known_face_names = []

        image_paths = listdir('img')

        for image_path in image_paths:
            timCook_image = load_image_file('img\\' + image_path)
            timCook_face_encoding = face_encodings(timCook_image)[0]
            self.known_face_encodings.append(timCook_face_encoding)
            self.known_face_names.append(image_path.split('.')[0])

    def know_images(self):
        small_frame = resize(self.frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        self.error_known = 1
        self.my_face_locations = face_locations(rgb_small_frame)
        my_face_encodings = face_encodings(rgb_small_frame, self.my_face_locations)

        self.face_names = []

        for face_encoding in my_face_encodings:
            matches = compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_distance(self.known_face_encodings, face_encoding)
            best_match_index = argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

                if name not in self.names:
                    self.names.append(name)
                    self.lineEdit_command.setText(name + '打卡成功')
                    history_write(name + '打卡成功')

            self.face_names.append(name)

        self.error_known = 0


def Show_SignWindow():
    App = QtWidgets.QApplication(argv)
    App.setWindowIcon(QtGui.QIcon('sign.ico'))
    SignWindow = QtWidgets.QMainWindow()
    ui = UiSignWindow()
    ui.setupUi(SignWindow)
    SignWindow.show()
    exit(App.exec_())


if __name__ == '__main__':
    Show_SignWindow()
