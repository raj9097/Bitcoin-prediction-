import statistics as st
print("hello Raj\n")
a=[20,10,50,10,21,90]
s=st.mode(a)
print("Mode",s)
m=st.mean(a)
print("Mean :",m)
median=st.median(a)
print("Meadian",median)

import numpy as np
b=np.array([[10,20,50,10],[1,2,3,5]])
print(b)
print("Dim:",b.ndim)

b=np.array([[10,20,30,50,10],[1,2,3,5,6],[1,1,1,1,1]])

print(b)
print("Dim:",b.ndim)
print("shape",b.shape)
print("Size",b.size)
print("Item Size",b.itemsize)
print("Data type ",b.dtype)

c=np.empty((5,5))
print(c)
f=np.full((3,3),5)
print(f)

d=np.arange(0,100,2)
print(d)


e=np.reshape(d,(10,5))
t=np.reshape(e,(2,5,5))
print(t)
print("Last element : ",d[10])
print("Element upto 10:",d[:10])
print("Last 5 element : ",d[-5:])
print("alternative  number :",d[::2])

#pandas 
import pandas as pd
p_dict={'pid':[1,2,3,4,5],'value':[10,20,30,40,50,]}
print(p_dict)
grt=pd.DataFrame(p_dict)
print(grt)