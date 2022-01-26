import re
def arithmetic_arranger(problems, cond=False):
  z = []
  pr =''
  se =''
  te =''
  qua =''
  fin = ''
  cond3 = False
  for x in problems:
    if x != True:
      z.append(getstr(x));
    #else:
    #  cond = True;
 

  for y in z:
    if y[0] == False:
      fin = 'Error: Numbers cannot be more than four digits.'
      cond3 = True
      break
    if len(z) > 5:
      fin = 'Error: Too many problems.'
      cond3 = True
      break
    if y[2] == False:
      fin = "Error: Operator must be '+' or '-'."
      cond3 = True
      break
    if y[3] == False:
      fin = 'Error: Numbers must only contain digits.'
      cond3 = True
      break
    pr = pr + " "*(y[3]-len(y[0])) + y[0] + " "*4;
    se = se + y[2] + " "*(y[3]-len(y[1])-1) + y[1] + " "*4
    te = te + "-"*y[3] + " "*4
    if cond == True:
      qua = qua + " "*(y[3]-len(str(y[4]))) +str(y[4])+ " "*4
  if cond3 == False:
    fin = pr[:-4] +"\n" + se[:-4] +"\n" + te[:-4]
    if cond == True:
      fin = fin +"\n" + qua[:-4]
  return fin

def getstr(str):
  if (len(re.search("\d*",str)[0]) > 4 or len(re.search("\d*$",str)[0]) > 4):
    fir = False
    fir2 = False
    fir4 = True
  else:
    fir = re.search("\d*",str)[0]
    fir2 = re.search("\d*$",str)[0]    
    if len(fir) > len(fir2):
      fir4 = len(fir) + 2
    else:
      fir4 = len(fir2) + 2 
  if re.search("[+]|[-]",str) == None:
    fir3 = False;
  else:
    fir3 = re.search("[+]|[-]",str)[0]
  try:
    fir5 = eval(str)
  except:
    fir5 = False
  if re.search("[a-z]",str,re.IGNORECASE):
    fir4 = False
  return [fir,fir2,fir3,fir4,fir5]
  

