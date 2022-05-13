import numpy as lmstar
A = lmstar.array([[1,3,5],[3,-4,2],[3,11,13]])
b= lmstar.array([-2,7,2])
c= lmstar.linalg.solve(A,b)
print(c)

