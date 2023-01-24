from asyncio.windows_events import NULL
from inspect import _empty
from pickle import EMPTY_DICT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
from atlassian import xray


class Ui_Form(object):
    def project_name_empty(self):
        self.project_name = self.lineEdit.text()
        if len(self.project_name) == 0 :
            msg1=QMessageBox()
            msg1.setWindowTitle("ERROR")
            msg1.setText("Project name cannot be empty")
            msg1.setIcon(QMessageBox.Critical)
            msg1.exec_()
        else :

            self.create_test_set()


    def create_test_set(self):
        from jira import JIRA
        jira= JIRA('URL',basic_auth=('Email_id', 'API Token'))
        summary=["Performance" , "Loading Times" , "Hardware Compatibility" , "Platform Features" , "Freezes & Crashes" , "User Spawning" , "Object Spawning Behaviour" , "NPC-Avatar Appearance","Explanatory Sequences","Training Guidance","Interactions","Interaction Feedback","Accessibility","UI System","Localization","Geometry","Lighting","Shading-Texturing","Collisions and View Blockers","Showroom Guidance","Branding","Audio","Multiplayer"]
        for y in summary:
            issue_dict = {
                'project': {'key': 'XR'},
                'summary': "["+self.project_name+"]"+"[QP] - "+y,
                'issuetype': {'name': 'Test Set'}
            }
            new_issue = jira.create_issue(fields=issue_dict)
            print("["+self.project_name+"]"+"[QP] - "+y)
        msg=QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Test Sets have been created")
        msg.exec_()
        exit()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 79)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 201, 20))
        self.lineEdit.setObjectName("lineEdit")  

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 125, 18))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.pushButton_create = QtWidgets.QPushButton(Form)
        self.pushButton_create.setGeometry(QtCore.QRect(225, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_create.clicked.connect(self.project_name_empty)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test Set Generator"))
        self.label.setText(_translate("Form", "Enter project name"))
        self.pushButton_create.setText(_translate("Form", "Create"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowIcon(QtGui.QIcon('.png'))
    Form.show()
    sys.exit(app.exec_())
