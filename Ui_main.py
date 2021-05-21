# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 406)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.opt_a = QtWidgets.QLineEdit(Dialog)
        self.opt_a.setReadOnly(True)
        self.opt_a.setClearButtonEnabled(False)
        self.opt_a.setObjectName("opt_a")
        self.horizontalLayout.addWidget(self.opt_a)
        self.chs_opt_a = QtWidgets.QPushButton(Dialog)
        self.chs_opt_a.setObjectName("chs_opt_a")
        self.horizontalLayout.addWidget(self.chs_opt_a)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.opt_b = QtWidgets.QLineEdit(Dialog)
        self.opt_b.setReadOnly(True)
        self.opt_b.setClearButtonEnabled(False)
        self.opt_b.setObjectName("opt_b")
        self.horizontalLayout_2.addWidget(self.opt_b)
        self.chs_opt_b = QtWidgets.QPushButton(Dialog)
        self.chs_opt_b.setObjectName("chs_opt_b")
        self.horizontalLayout_2.addWidget(self.chs_opt_b)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.opt_ok = QtWidgets.QLineEdit(Dialog)
        self.opt_ok.setReadOnly(True)
        self.opt_ok.setClearButtonEnabled(False)
        self.opt_ok.setObjectName("opt_ok")
        self.horizontalLayout_3.addWidget(self.opt_ok)
        self.chs_opt_ok = QtWidgets.QPushButton(Dialog)
        self.chs_opt_ok.setObjectName("chs_opt_ok")
        self.horizontalLayout_3.addWidget(self.chs_opt_ok)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.chs_predict_file = QtWidgets.QPushButton(Dialog)
        self.chs_predict_file.setObjectName("chs_predict_file")
        self.verticalLayout.addWidget(self.chs_predict_file)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.opt_a.setPlaceholderText(_translate("Dialog", "A类输出位置"))
        self.chs_opt_a.setText(_translate("Dialog", "选择A类输出位置"))
        self.opt_b.setPlaceholderText(_translate("Dialog", "B类输出位置"))
        self.chs_opt_b.setText(_translate("Dialog", "选择B类输出位置"))
        self.opt_ok.setPlaceholderText(_translate("Dialog", "OK类输出位置"))
        self.chs_opt_ok.setText(_translate("Dialog", "选择OK类输出位置"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:xx-large; font-weight:600;\"><br /></h1></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "待检测图片"))
        self.chs_predict_file.setText(_translate("Dialog", "选择待检测图片"))
        self.pushButton.setText(_translate("Dialog", "开始执行检测"))
