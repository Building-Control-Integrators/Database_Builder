from os import startfile
from shutil import copyfile


def create_excel_workbook():
    copyfile('assets/template_pl.xlsx', 'Points List Template.xlsx')
    startfile('Points List Template.xlsx')

