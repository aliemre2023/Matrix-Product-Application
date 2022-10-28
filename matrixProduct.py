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

matrix1 = input("Input 9 number for matrix 1 (separate with comma[,]): ").split(",")
matrix2 = input("Input 9 number for matrix 2 (separate with comma[,]): ").split(",")

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
            pri = m1[i][x] * m2[x][j]
            answer.append(pri)

realAnswer = list()
o = 0
for i in range(9):
    total = answer[o]+answer[o+1]+answer[o+2]
    o += 3
    realAnswer.append(total)

final = np.array(realAnswer).reshape(3,3)

print("{0} (1st matrix)\n *\n {1} (2nd matrix)\n =\n {2} (answer)".format(m1,m2,final))










