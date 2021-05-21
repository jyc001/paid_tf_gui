import Ui_main
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys, qt_material, predict


class Ui(Ui_main.Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.picfs = None
        self.flag = False
        self.step = 0

    def setupUi(self):
        super().setupUi(self)
        self.chs_opt_ok.clicked.connect(self.chs_ok_clk)
        self.chs_opt_a.clicked.connect(self.chs_A_clk)
        self.chs_opt_b.clicked.connect(self.chs_B_clk)
        self.chs_predict_file.clicked.connect(self.chs_pic_clk)
        self.pushButton.clicked.connect(self.start_btn_clk)

    def opendic(self, title):
        dir_gt = QFileDialog.getExistingDirectory(self, title)
        if dir_gt == "":
            return None
        else:
            return dir_gt

    def chs_ok_clk(self):
        gg_dir = self.opendic("选择ok类输出目录")
        if gg_dir is not None:
            predict.ok_output = gg_dir
            self.opt_ok.setText(gg_dir)

    def chs_A_clk(self):
        gg_dir = self.opendic("选择A类输出目录")
        if gg_dir is not None:
            predict.defect_A_output = gg_dir
            self.opt_a.setText(gg_dir)

    def chs_B_clk(self):
        gg_dir = self.opendic("选择B类输出目录")
        if gg_dir is not None:
            predict.defect_B_output = gg_dir
            self.opt_b.setText(gg_dir)

    def chs_pic_clk(self):
        gg_dir = QFileDialog.getOpenFileNames(self, "选择待检测图片", filter="JPG Img(*.jpg)")
        if gg_dir is not None:
            self.picfs = gg_dir[0]
            show_text = ""
            for i in self.picfs:
                show_text += i + "\n"
            self.textEdit.setText(show_text)

    def update_flag(self):
        if predict.ok_output is not None and predict.defect_A_output is not None and predict.defect_B_output is not None:
            self.flag = True

    def start_btn_clk(self):
        self.update_flag()
        if not self.flag:
            print("文件未选择完成")
            return
        self.progressBar.setMaximum(len(self.picfs))
        for i in self.picfs:
            predict.predict(i)
            self.step +=1
            self.progressBar.setValue(self.step)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a_ui = Ui()
    qt_material.apply_stylesheet(app, theme="dark_blue.xml")
    a_ui.setupUi()
    a_ui.show()
    sys.exit(app.exec())
