List=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
emptylist=[]
for i in range(0,len(List)-1):
  emptylist.append(int(List[i][1]))
t=[]
func_1=lambda t: t.append(max(emptylist))
func_2=lambda t: t.append(min(emptylist))
func_1(t)
func_2(t)
print("Maximum and minimum values of the said list of tuples: ",tuple(t))
