# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:04:42 2021

@author: GOWTHAM
"""


import pandas as pd

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            li=i
            #li.append(i)
            #li.append(x.index(v))
            return li
        
        
df = pd.read_excel (r'C:\studies\project phase1\review\c432seq.xlsx')
#print(df,"\n")
PI=(df.values[0][0])
PO=(df.values[0][1])
#print(PI,"\n",PO)
netlist=[]
#print(netlist)
#for i in range(2,len(df)):
    #print("\n",i)
 #   for j in range(0,len(df.values[0])):
  #      print(j,end=" ")
netname=[]
for i in range(2,len(df)):
 #   print("\n",i)
    for j in range(2,len(df.values[0])):
        #print(df.values[i][j],end=" ")
        if df.values[i][j] in netname:
            continue
        else:
            netname.append(df.values[i][j])

print("\nNetnames= ",netname)
net_tp=[]
netname_r=[]
for i in range(0,len(netname)):
    if str(netname[i]) in PI:
        net_tp.append([netname[i],0.5,0.5])
#    if netname[i] in PO:
 #       continue
  #  else:
   #     netname_r.append(netname[i])
#print("\n",net_tp)
#print(net_tp)
Transition_Prob=[]
for i in range(2,len(df)):
    x=str(df.values[i][2])
    print(df.values[i][1])
    if(df.values[i][0]=="nand"):
        if "NAND2" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
#            print((p))
#            print(df.values[i][1],net_tp[p[0]],p[0])
#
#            print(df.values[i][1],net_tp[p[1]],p[1])

            form=[]
            x1=net_tp[p[0]][2]*net_tp[p[1]][2]
            x2=net_tp[p[0]][1]+net_tp[p[1]][1]-(net_tp[p[0]][1]*net_tp[p[1]][1])
            form.append(x1)
            form.append(x2)
           # print(form)
        if "NAND3" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            p.append(index_2d(net_tp,df.values[i][5]))
            #print((p))
            #print(df.values[i][1],net_tp[p[0]],p[0])     asd  pr1(1) * pr2(1)

            #print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x1=net_tp[p[0]][2] *net_tp[p[1]][2]*net_tp[p[2]][2]
            x2=net_tp[p[0]][1]+net_tp[p[1]][1]+net_tp[p[2]][1]-(net_tp[p[0]][1]*net_tp[p[1]][1]*net_tp[p[2]][1])
            form.append(x1)
            form.append(x2)
            #print(form)
        if "NAND4" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            p.append(index_2d(net_tp,df.values[i][5]))
            p.append(index_2d(net_tp,df.values[i][6]))
            #print("\n",p)
            #print(df.values[i][1],net_tp[p[0]],p[0])     

            #print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x1=net_tp[p[0]][2] *net_tp[p[1]][2]*net_tp[p[2]][2]*net_tp[p[3]][2]
            x2=1-(net_tp[p[0]][2] *net_tp[p[1]][2]*net_tp[p[2]][2]*net_tp[p[3]][2])
            form.append(x1)
            form.append(x2)
            print("\n")
            print("\n")
            print(form)
            print(net_tp[p[0]])
            
            print(net_tp[p[1]])
            print("\n")
            
    if(df.values[i][0]=="not"):
        if "NOT" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            form=[]
#            print((p))
#            print(df.values[i][1],net_tp[p[0]],p[0])
            x1=net_tp[p[0]][2] 
            x2=net_tp[p[0]][1]
            form.append(x1)
            form.append(x2)
            #print(form)
    if(df.values[i][0]=="nor"):
        if "NOR2" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            #print((p))
#            print(df.values[i][1],net_tp[p[0]],p[0])
#
#            print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x2=net_tp[p[0]][1] *net_tp[p[1]][1]
            x1=net_tp[p[0]][2]+net_tp[p[1]][2]-(net_tp[p[0]][2]*net_tp[p[1]][2])
            form.append(x1)
            form.append(x2)
    if(df.values[i][0]=="xor"):
        if "XOR2" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            #print((p))
#            print(df.values[i][1],net_tp[p[0]],p[0])
#
#            print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x1=(net_tp[p[0]][1]*net_tp[p[1]][1])+(net_tp[p[0]][2] *net_tp[p[1]][2])
            x2=(net_tp[p[0]][1]-net_tp[p[1]][2])+(net_tp[p[0]][1]*net_tp[p[1]][2])
            form.append(x1)
            form.append(x2)
    if(df.values[i][0]=="and"):
        if "AND8" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            p.append(index_2d(net_tp,df.values[i][5]))
            p.append(index_2d(net_tp,df.values[i][6]))
            p.append(index_2d(net_tp,df.values[i][7]))
            p.append(index_2d(net_tp,df.values[i][8]))
            p.append(index_2d(net_tp,df.values[i][9]))
            p.append(index_2d(net_tp,df.values[i][10]))
            #print("\n\n\n",p)
            #print(df.values[i][1],net_tp[p[0]],p[0])     asd  pr1(1) * pr2(1)

            #print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x2=net_tp[p[0]][2] *net_tp[p[1]][2]*net_tp[p[2]][2]*net_tp[p[3]][2]*net_tp[p[4]][2] *net_tp[p[5]][2]*net_tp[p[6]][2]*net_tp[p[7]][2]
            x1=net_tp[p[0]][1] +net_tp[p[1]][1]+net_tp[p[2]][1]+net_tp[p[3]][1]+net_tp[p[4]][1] +net_tp[p[5]][1]+net_tp[p[6]][1]+net_tp[p[7]][1]-(net_tp[p[0]][1]*net_tp[p[1]][1]*net_tp[p[2]][1]*net_tp[p[3]][1]*net_tp[p[4]][1]*net_tp[p[5]][1]*net_tp[p[6]][1]*net_tp[p[7]][1])
            form.append(0.5)
            form.append(0.5)
            #print(form)
        if "AND9" in df.values[i][1]:
            p=[]
            p.append(index_2d(net_tp,df.values[i][3]))
            p.append(index_2d(net_tp,df.values[i][4]))
            p.append(index_2d(net_tp,df.values[i][5]))
            p.append(index_2d(net_tp,df.values[i][6]))
            p.append(index_2d(net_tp,df.values[i][7]))
            p.append(index_2d(net_tp,df.values[i][8]))
            p.append(index_2d(net_tp,df.values[i][9]))
            p.append(index_2d(net_tp,df.values[i][10]))
            p.append(index_2d(net_tp,df.values[i][11]))
            #print("\n\n\n",p)
            #print(df.values[i][1],net_tp[p[0]],p[0])     asd  pr1(1) * pr2(1)

            #print(df.values[i][1],net_tp[p[1]],p[1])
            form=[]
            x2=net_tp[p[0]][2] *net_tp[p[1]][2]*net_tp[p[2]][2]*net_tp[p[3]][2]*net_tp[p[4]][2] *net_tp[p[5]][2]*net_tp[p[6]][2]*net_tp[p[7]][2]*net_tp[p[8]][2]
            
            x1=net_tp[p[0]][1] +net_tp[p[1]][1]+net_tp[p[2]][1]+net_tp[p[3]][1]+net_tp[p[4]][1] +net_tp[p[5]][1]+net_tp[p[6]][1]+net_tp[p[7]][1]+net_tp[p[8]][1]-(net_tp[p[0]][1]*net_tp[p[1]][1]*net_tp[p[2]][1]*net_tp[p[3]][1]*net_tp[p[4]][1]*net_tp[p[5]][1]*net_tp[p[6]][1]*net_tp[p[7]][1]*net_tp[p[8]][1])
            form.append(0.5)
            form.append(0.5)
           # print(form)
            
            
        
        #print(l)     pr1(0) + pr2(0)-[pr1(0) * pr2(0)]
    net_tp.append([x,form[0],form[1]])        
ll=(len(net_tp))
for i in range(0,ll):
    Transition_Prob.append([net_tp[i][0],net_tp[i][1]*net_tp[i][2]])
print("\n",net_tp)
df1=pd.DataFrame(net_tp,columns=["Netname","Probability of 0","Probability of 1"])
df2=pd.DataFrame(Transition_Prob,columns=["Netname","Transition Probability"])
print("\n",df1,"\n\n",df2)