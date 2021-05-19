import sys
import Database_ZOB_Builder
from PyQt5 import QtWidgets, Qt, QtCore
from open_file_dialog import open_fd
from generate_new_excel_template import create_excel_workbook


# generate a new excel workbook from template
def create_new_workbook():
    create_excel_workbook()
    pass


# ZOB Creation
def create_zob_objects():
    pass


# load an excel workbook
def load_file():
    file_path = open_fd()
    if file_path == '':
        return ''
    if file_path.find('.xlsx') == -1:
        wrong_file_type_popup = QtWidgets.QMessageBox()
        wrong_file_type_popup.setIcon(QtWidgets.QMessageBox.Critical)
        wrong_file_type_popup.setWindowTitle('Database Builder')
        wrong_file_type_popup.setText('Incorrect file type. File must be .xlsx file format.')
        wrong_file_type_popup.exec_()
        return 0
    if file_path != '':
        ui.file_path_string.setText(file_path)
        return file_path


# Main loop
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Database_ZOB_Builder.Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    # Menu actions
    ui.actionClose.triggered.connect(sys.exit)
    ui.actionNewExcelTemplate.triggered.connect(create_new_workbook)

    # Main window buttons
    ui.create_zob_button.clicked.connect(create_zob_objects)
    ui.load_file_button.clicked.connect(load_file)
    ui.close_button.clicked.connect(sys.exit)

    sys.exit(app.exec_())

