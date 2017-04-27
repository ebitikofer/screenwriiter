#makefile

PY3 = python3
CMD = screenwriiui.py
DEL = rm -vf
ETE = out.tex out.log out.aux out.pdf ./txtsrc/out.tex

run:
	$(PY3) $(CMD)

install:
	sudo apt-get install python-qt4

clean:
	$(DEL) $(ETE)
