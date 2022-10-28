import numpy as np
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

print("""
___3x3 MATRİX PRODUCT APPLİCATİON___

The first 3 numbers you enter will form the 1st line, the next 3 numbers 
will form the 2nd line, and the other 3 numbers will form the 3rd line.
Please enter only 9 numbers or application will not work.

""")

matrix1 = input("Input 9 number for matrix 1 (seperate with comma[,]): ").split(",")
matrix2 = input("Input 9 number for matrix 2 (seperate with comma[,]): ").split(",")

n1 = np.array(matrix1)
n2 = np.array(matrix2)

n1 = n1.astype(np.float)
n2 = n2.astype(np.float)

m1 = np.array(n1).reshape([3,3])
m2 = np.array(n2).reshape([3,3])

answer = list()
for i in range(3):
    for j in range(3):
        for x in range(3):
            pro = m1[i][x] * m2[x][j]
            answer.append(pro)

donus = 0
tot11 = 0
tot12 = 0
tot13 = 0
tot21 = 0
tot22 = 0
tot23 = 0
tot31 = 0
tot32 = 0
tot33 = 0
while donus < 3:
    tot11 += answer[donus]
    donus += 1
while donus < 6:
    tot12 += answer[donus]
    donus += 1
while donus < 9:
    tot13 += answer[donus]
    donus += 1
while donus < 12:
    tot21 += answer[donus]
    donus += 1
while donus < 15:
    tot22 += answer[donus]
    donus += 1
while donus < 18:
    tot23 += answer[donus]
    donus += 1
while donus < 21:
    tot31 += answer[donus]
    donus += 1
while donus < 24:
    tot32 += answer[donus]
    donus += 1
while donus < 27:
    tot33 += answer[donus]
    donus += 1

realAnswer = list()
realAnswer.append(tot11)
realAnswer.append(tot12)
realAnswer.append(tot13)
realAnswer.append(tot21)
realAnswer.append(tot22)
realAnswer.append(tot23)
realAnswer.append(tot31)
realAnswer.append(tot32)
realAnswer.append(tot33)

final = np.array(realAnswer).reshape(3,3)

print("{0} (1st matrix)\n *\n {1} (2nd matrix)\n =\n {2} (answer)".format(m1,m2,final))










