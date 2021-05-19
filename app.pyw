import sys
import Database_ZOB_Builder
from PyQt5 import QtWidgets, Qt, QtCore
from open_file_dialog import open_fd


# ZOB Creation
def create_zob_objects():
    pass


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
    print(QtWidgets.QStyleFactory.keys())
    window = QtWidgets.QMainWindow()
    ui = Database_ZOB_Builder.Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    # Menu actions
    ui.actionClose.triggered.connect(sys.exit)

    # Main window buttons
    ui.create_zob_button.clicked.connect(create_zob_objects)
    ui.load_file_button.clicked.connect(load_file)
    ui.close_button.clicked.connect(sys.exit)

    sys.exit(app.exec_())

