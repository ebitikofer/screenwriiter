import sys
import subprocess
import re
from PyQt4 import QtCore, QtGui, uic
import screenwriiter

qtCreatorFile = "gui/screenwriiter.ui" # Enter file here.

entries = []
selected = 0

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class screenwriiter_gui(QtGui.QMainWindow, Ui_MainWindow):

  def __init__(self):
      QtGui.QMainWindow.__init__(self)
      Ui_MainWindow.__init__(self)
      self.setupUi(self)
      self.load()
      self.block_list.currentItemChanged.connect(self.edit)
      self.compose_button.clicked.connect(self.update)
      self.plus_button.clicked.connect(self.add_block)
      self.minus_button.clicked.connect(self.sub_block)
      self.compose_button.clicked.connect(self.compose)

  def load(self):
    inf = open("txtsrc/save.txt", 'r')
    entry = []
    store = False
    for line in inf:
      if store is True:
        entry.append(line[:-1])
        entries.append(entry)
        store = False
        entry = []
      elif line[0:3] == '-->':
        entry.append(line[:-1])
        store = True
        continue
    inf.close()
    self.update()

  def update(self):
    self.block_list.clear()
    outf = open("txtsrc/body.txt", 'w')
    for entry in entries:
      item = QtGui.QListWidgetItem(entry[0][3:-3])
      self.block_list.addItem(item)
      outf.write(entry[0] + "\n")
      outf.write(entry[1] + "\n")
      outf.write("\n")
    outf.close()
    #update list

  def edit(self):
    self.text_box.setPlainText(entries[self.block_list.currentRow()][1])
    #update list

  def add_block(self):
    entry = []
    #i = selected + 1 #or last if none selected maybr use insert into list
    entry.append(str(self.type_box.currentText()))
    entry.append(str(self.text_box.toPlainText()))
    entries.insert(self.block_list.currentRow(), entry)
    self.text_box.setPlainText("TEXT")
    self.update()

  def sub_block(self):
    entries.pop(self.block_list.currentRow())
    self.update()

  def compose(self):
    with open('out.tex', 'w') as f:
        subprocess.call(['python3', 'screenwriiter.py'], stdout=f)
    subprocess.run(['pdflatex', 'out.tex'])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = screenwriiter_gui()
    window.show()
    sys.exit(app.exec_())
