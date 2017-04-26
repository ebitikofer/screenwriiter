import sys
import subprocess
import re
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "gui/screenwriiter.ui" # Enter file here.

entries = []
selected = 0

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class screenwriiter_gui(QtGui.QMainWindow, Ui_MainWindow):

  def __init__(self):
      QtGui.QMainWindow.__init__(self)
      Ui_MainWindow.__init__(self)
      self.setupUi(self)
      self.compose_button.clicked.connect(self.update)
      self.plus_button.clicked.connect(self.add_block)
      self.minus_button.clicked.connect(self.sub_block)
      self.compose_button.clicked.connect(self.compose)

  def update(self):
    selected = 0
    #update list

  def add_block(self):
    entry = []
    #i = selected + 1 #or last if none selected maybr use insert into list
    entry.append(str(self.type_box.currentText()))
    entry.append(str(self.text_box.toPlainText()))
    entries.insert(selected + 1, entry)
    self.text_box.setPlainText("TEXT")
    item = QtGui.QListWidgetItem(self.type_box.currentText())
    self.block_list.insertItem(self.block_list.currentRow(), item)

  def sub_block(self):
    entries.pop(self.block_list.currentRow())
    self.block_list.takeItem(self.block_list.currentRow())
    #delete selected item
    #remove and decrement remaining indices

  def compose(self):
    with open('out.tex', 'w') as f:
        subprocess.call(['python3', 'screenwriiter.py'], stdout=f)
    subprocess.run(['pdflatex', 'out.tex'])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = screenwriiter_gui()
    window.show()
    sys.exit(app.exec_())
