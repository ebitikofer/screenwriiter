#makefile

PY3 = python3
CMD = screenwriiui.py
DEL = rm -vf
ETE = out.tex out.log out.aux out.pdf ./txtsrc/out.tex

run:
	$(PY3) $(CMD)

install:
	sudo apt-get install python3
	sudo apt-get install python3-pyqt4
	sudo apt-get install python3-poppler-qt4
	sudo apt-get install texlive

clean:
	$(DEL) $(ETE)
