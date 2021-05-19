from PyQt5.QtWidgets import QFileDialog


def open_fd():
    file_path = QFileDialog.getOpenFileName(filter='*xlsx')
    return file_path[0]
