import sys
import re

def make_env():

  inf = open("txtsrc/init.txt", 'r')
  vals = []
  for line in inf:
    vals.append(line[:-1]),

  print(r'\documentclass[12pt]{' + vals[0] + '}')
  print(r'\usepackage[utf8]{inputenc}')
  print(r'\usepackage[letterpaper, margin=1in, left=1.5in]{geometry}')
  #print(r'\usepackage[document]{ragged2e}')
  print(r'\usepackage{tgbonum}')
  print(r'\linespread{.8}')
  #print(r'\textwidth=6in')
  print(r'\title{' + vals[1] + '}')
  print(r'\author{' + vals[2] + '}')
  print(r'\date{' + vals[3] + '}')
  print(r'\begin{document}')

  print(r'{\fontfamily{qcr}\selectfont')
  make_body()
  print(r'}')
  print(r'\end{document}')

  inf.close()

def make_body():

  t12h = r'\setlength{\hsize}{6in}'
  t8h = r'\setlength{\hsize}{4in}'
  t7h = r'\setlength{\hsize}{3.5in}'
  t5h = r'\setlength{\hsize}{2.5in}'
  t4h = r'\setlength{\hsize}{2in}'
  i0h = r'\setlength{\leftskip}{0in}'
  i2h = r'\setlength{\leftskip}{1in}'
  i3h = r'\setlength{\leftskip}{1.5in}'
  i4h = r'\setlength{\leftskip}{2in}'
  i8h = r'\setlength{\leftskip}{4in}'

  s1 = "\n"
  endl = r'\\'
  ext = r'~\\'
  ind = r'\indent '
  nnd = r'\noindent '

  shc = 0
  pc = 0
  tc = 0
  sc = 0

  pn = ''
  ex = ''
  pnf = False
  exf = False

  inf = open("txtsrc/body.txt", 'r')
  symbols = []
  vals = []
  store = False
  for line in inf:
    if store is True:
      vals.append(line[:-1])
      symbols.append(vals)
      store = False
      vals = []
    elif line[0:3] == '-->':
      vals.append(line[3:-4])
      store = True
      continue
  inf.close()

  #bool auto_size
  #string length, width, s_title, img_name, img_l, img_w, scale

  print()
  print(r'\noindent FADE IN:\\')

  for symbol in symbols:

    if symbol[0] == "SLGL": #Indent: Left: 0.0" Right: 0.0" Width: 6.0"
      prf, loc, tm = symbol[1].upper().split(';')
      if prf == "E":
        prf = "EXT."
      elif prf == "I":
        prf = "INT."
      elif prf == "IE":
        prf = "INT./EXT."
      else:
        print("HEADING PRFIX INCORRECT")
      print(ext + t12h + i0h)
      print(nnd + prf + r' ' + loc + r' - ' + tm + endl)
      print()
    elif symbol[0] == "SUBH": #Indent: Left: 0.0" Right: 0.0" Width: 6.0"
      print(ext + t12h + i0h)
      print(symbol[1].upper())
      print()
      shc += 1
    elif symbol[0] == "ACTN": #Indent: Left: 0.0" Right: 0.0" Width: 6.0"
      print(t12h + i0h)
      print(nnd + symbol[1] + endl)
      print()
    elif symbol[0] == "CHAR": #Indent: Left: 2.0" Right: 0.0" Width: 4.0"
      nm, an = symbol[1].split(';')
      print(t12h + i0h)
      print(nnd + nm.upper() + r', ' + an + endl)
      print()
    elif symbol[0] == "DLOG": #Indent: Left: 1.0" Right: 1.5" Width: 3.5"
      nm, tx = symbol[1].split(';')
      if pnf == True:
        print(t12h + i4h)
        print(nnd + nm.upper() + ex)
        print()
        print(t5h + i3h)
        print(nnd + pn)
        print()
        print(t7h + i2h)
        print(nnd + tx + endl)
        print()
        pn = ''
        pnf = False
      else:
        print(t12h + i4h)
        print(nnd + nm.upper() + ex)
        print()
        print(t7h + i2h)
        print(nnd + tx + endl)
        print()
      if exf == True:
        ex = ''
        exf = False
      nm = ''
      tx = ''
    elif symbol[0] == "PNTL": #Indent: Left: 1.5" Right: 2.0" Width: 2.5
      pn = r'(' + symbol[1] + r')'
      pnf = True
      pc += 1
    elif symbol[0] == "EXTN": #Placed after the character's name, in parentheses
      ex = r' (' + symbol[1] + r')'
      exf = True
    elif symbol[0] == "TRSN": #Indent: Left: 4.0" Right: 0.0" Width: 2.0"
      print(t4h + i8h)
      print(nnd + symbol[1].upper() + endl)
      print()
      tc += 1
    elif symbol[0] == "SHOT": #Indent: Left: 0.0" Right: 0.0" Width: 6.0"
      print(t12h + i0h)
      print(nnd + symbol[1].upper() + endl)
      print()
      sc += 1

def main():
    make_env()

if __name__ == "__main__":
    main()
