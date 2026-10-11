import pandas as pd
from pandas.core.interchange import column

pd.read_csv("emp.csv")
df=pd.read_csv("emp.csv")
#print(df)
sres1=  df['ename']
'''
print(sres1)
print(type(sres1))
print(df.head())
sers2=df[["eno","ename","salary"]]
print(sers2.head(13))
#print(type(sers2))

df2=pd.read_csv("emp.csv", usecols=["eno", "ename","salary"], index_col="eno")
print(df2.iloc[3:11])
'''
# get the details of employees having salary > 50000 and  / or department id 30.
df3=pd.read_csv("emp.csv", index_col="eno")
'''print(df3)
print(type(df3))
filter1=df3['salary']>50000
filter2=df3['deptno']==30
#print(df3[filter1 & filter2])
print(df3[filter1 | filter2])

print(f"{df3[(df3['salary']>50000) & (df3['deptno']==30)]}")
## Q2. Get me all the employees who belongs to either deptno 10 or deptno 20
print(df[(df['deptno']==10) | (df['deptno']==20)])
#print(df[(df['deptno']==10) | (df['deptno']==20)].shape())
print(df[(df['deptno']==10) | (df['deptno']==20)].count())

## Q3. Get me all the employees who not belongs to deptno 10 or deptno 20
filter3=~((df['deptno']==10) | (df['deptno']==20))
print(df[filter3])

print(len(df[filter3]))
print(df[filter3].count())

# Sorting salary in descending order for all employees belongs to department 30

df4=pd.read_csv("emp.csv", usecols=["eno", "ename", "salary", "deptno"], index_col="eno")
df4_sorted=df4[(df4['deptno']==30)].sort_values(by="salary", ascending=False)
print(df4_sorted)
# skip rows and show limited rows
print(df)
print(df.dtypes)
df6=pd.read_csv("emp.csv", skiprows=10, nrows=10, header=None, names=["eno", "ename", "salary", "deptno"])
print(df6)

#print(df5)

# date handling
df5=pd.read_csv("emp.csv", parse_dates=['doj'])
print(df5.dtypes)
df5['doj']=df5['doj'].dt.year
df5.rename(columns={'doj': 'year'}, inplace=True)
print(df5.head())
df5['doj']=df5['year'].dt.month
df5.rename(columns={'doj': 'month'}, inplace=True)
print(df5.head())
df5['doj']=df5['doj'].dt.day
df5.rename(columns={'doj': 'date'}, inplace=True)
print(df5.head())

#filter based on month and years.
df5=pd.read_csv("emp.csv", parse_dates=['doj'])
#df5['doj']=df5['doj'].dt.year
filter_years=(df5['doj'].dt.year>2017) & (df5['doj'].dt.month>6)
#df5.rename(columns={'doj': 'year'}, inplace=True)
print(df5[filter_years])
'''
#without parse_Dates no dt operation working
df5=pd.read_csv("emp.csv", parse_dates=['doj'])
filter_years=(df5['doj'].dt.year>2017) & (df5['doj'].dt.month>6)
print(df5[filter_years].count())
print(df5.shape)

# working of Sort_index