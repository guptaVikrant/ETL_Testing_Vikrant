import pandas as pd

df1=pd.read_csv("Data/Employee.csv")
df2=pd.read_csv("Data/Department.csv")
# Count the employee in each department
df_empCount=df1.groupby("DeptID")["EmpID"].count()
print(df_empCount)
print(df_empCount.reset_index())
'''
#get the total count of employees, max salary, min salary, total salary, avg in each department
aggr_data=df1.groupby("DeptID")['Salary'].agg(['count', 'sum', 'min', 'max']).reset_index()
aggr_data.rename(columns={'count': 'Employee_count', 'sum': 'total_Salary', 'min': 'Minimum_Salary',  'max': 'Max_Salary'}, inplace=True)
print(aggr_data)
# Write the summary into csv file
aggr_data.to_csv("emp_Summary1.csv", index=False)
print(f"Summary report has been created",end="\n")
print(f"{pd.read_csv('emp_Summary1.csv')}")
'''
#1. merge() - SQL-like Join Operatio
print(df1.head())
print(df2.dtypes)
'''df1 = df1.astype({
    'DeptID': 'int64',
    'Salary': 'float64',
})
df2 = df2.astype({'Location': 'str'})
print(df2.dtypes)
print(df2.head())
print(df1.merge(df2, on='DeptID', how='inner'))

# Merge 2 files Employee and Department based on DeptID
inner_joined=df1.merge(df2, on='DeptID', how='inner')[['Name','DeptName']]
left_joined=df1.merge(df2, on='DeptID', how='left')[['Name','DeptName']]
right_joined=df1.merge(df2, on='DeptID', how='right')[['Name','DeptName']]
print("left_joined", end="\n")
print(left_joined)
print("right_joined", end="\n")
print(right_joined)
print("inner_joined",end="\n")
print(inner_joined)
inner_Joined_withCond=df1[['Name','DeptID']].merge(df2[['DeptID','DeptName']][df2['DeptName']=='HR'], on='DeptID', how='inner')[['Name','DeptName']]
print(inner_Joined_withCond)



# Assignment #1 A CSV file containing employee’s details with duplicate
#records, write a script to get all the records which are duplicates in the file in result dataframe.
duplicates = df1[df1.duplicated(keep=False)]
print(duplicates)

# # Assignment #2) Fetch all the deptno which are having more than 5 employees working in it.
# using having in sql
aggr_df=df1.groupby('DeptID')['EmpID'].count().reset_index()
print(aggr_df)
aggr_df.rename(columns={'EmpID':'Employee_count'}, inplace=True)
print(aggr_df.columns)
print(aggr_df[aggr_df['Employee_count']>2])
'''