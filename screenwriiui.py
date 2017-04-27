import sys
import subprocess
import re
from PyQt4 import QtCore, QtGui, uic
import screenwriiter

qtCreatorFile = "gui/screenwriiter.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class screenwriiter_gui(QtGui.QMainWindow, Ui_MainWindow):

  def __init__(self):
      QtGui.QMainWindow.__init__(self)
      Ui_MainWindow.__init__(self)
      self.setupUi(self)
      self.action_New.triggered.connect(self.new)
      self.action_Open.triggered.connect(self.load)
      self.action_Save_as.triggered.connect(self.save)
      self.blocks.currentItemChanged.connect(self.edit)
      self.compose_button.clicked.connect(self.update)
      self.plus_button.clicked.connect(self.add)
      self.minus_button.clicked.connect(self.sub)
      self.compose_button.clicked.connect(self.compose)
      self.entries = []


  def new(self):
    self.entries = []
    self.update()
    self.text_box.setPlainText("TEXT")

  def load(self):
    inf = open("save/save.txt", 'r')
    self.entries = []
    entry = []
    store = False
    for line in inf:
      if store is True:
        entry.append(line[:-1])
        self.entries.append(entry)
        store = False
        entry = []
      elif line[0:3] == '-->':
        entry.append(line[:-1])
        store = True
        continue
    inf.close()
    self.update()

  def save(self):
    outf = open("txtsrc/body.txt", 'w')
    for entry in self.entries:
      outf.write(entry[0] + "\n")
      outf.write(entry[1] + "\n")
      outf.write("\n")
    outf.close()
    #update list

  def update(self):
    self.blocks.clear()
    for entry in self.entries:
      item = QtGui.QListWidgetItem(entry[0][3:-3])
      self.blocks.addItem(item)
    #update list

  def edit(self):
    self.text_box.setPlainText(self.entries[self.blocks.currentRow()][1])
    #text = QtGui.QPlainTextEdit(entry[0][3:-3])
    #self.blocks.addItem(item)
    #update list

  def add(self):
    entry = []
    #i = selected + 1 #or last if none selected maybr use insert into list
    entry.append(r'-->' + str(self.type_box.currentText()) + r'<--')
    entry.append(str(self.text_box.toPlainText()))
    self.entries.insert(self.blocks.currentRow(), entry)
    self.text_box.setPlainText("TEXT")
    self.update()

  def sub(self):
    self.entries.pop(self.blocks.currentRow())
    self.update()

  def compose(self):
    self.save()
    with open('out.tex', 'w') as f:
        subprocess.call(['python3', 'screenwriiter.py'], stdout=f)
    subprocess.run(['pdflatex', 'out.tex'])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = screenwriiter_gui()
    window.show()
    sys.exit(app.exec_())
