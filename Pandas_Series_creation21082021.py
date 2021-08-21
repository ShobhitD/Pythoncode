import pandas as pd

s1=pd.Series(dtype="int32")  #empty series
print(s1)

s2=pd.Series(["A","B","C"]) #series of object 
print(s2)

s3=pd.Series([15.8,-16.5,14.1,56.7]) #series of float literals 
print(s3)

s4=pd.Series([14,"ABC",15]) #series of mixed data types
print(s4)

#bool<int<float<complex<object ORDER OF PRECEDENCE

s5=pd.Series([14,16.5,-5,15.4]) #series of mixed data types
print(s5)

s6=pd.Series([4,7,5,6],dtype="float64") #explicit conversion of dtype
print(s6)

s7=pd.Series([4,7.5,5.7,6],dtype="object") #explicit conversion of dtype
print(s7)

s11=pd.Series(5,index=[1,2,3],dtype="float64") #creating series object using scaler value
print(s11)

s12=pd.Series(8,index=['A','B','C'],dtype="float64") #creating series object using scaler value
print(s12)

s13=pd.Series(8,dtype="float64") 
print(s13)

s14=pd.Series(8.0, index=[1,2,3],dtype="int64") #creating series object using scaler value
print(s14)

s15=pd.Series([14,"ABC",15.75,True]) #series of mixed data types
print(s15)

s16=pd.Series(["154","158"],dtype="float64") #explicit conversion of dtype
print(s16)

"""
#explicit conversion of dtype here will give an error but noy in previous example. 
#String value which are non numeric cannot be converted to float64/int64 types
s16=pd.Series(["ABC","PQR"],dtype="float64") 
print(s16)
"""

s17=pd.Series(1,dtype="bool")  #explicit conversion of dtype
print(s17) 











