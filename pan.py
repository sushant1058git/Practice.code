
# import pandas as pd
# data = pd.read_csv("nba.csv")

# data.dropna(inplace=True)           #Removing null values to remove errors

# perc=[.2,.4,.6,.8]                  #Defining percentage values
# include=['object','float','int']    #List of dtypes to include    
# desc=data.describe(percentiles=perc,include=include) #calling describe function
# print(desc)


# import pandas as pd

# data=pd.read_csv('nba.csv')
# # print(data)
# data.dropna(inplace=True)
# desc=data["Name"].describe()
# print(desc)

# import pandas as pd

# # Define a dictionary containing employee data
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(data)
  
# # select two columns
# print(df[['Name', 'Qualification']])


# importing pandas module
# import pandas as pd
  
# making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name" )
# print(data)
  
# # dropping passed columns
# data.drop(["Team", "Weight"], axis = 1, inplace = True)
  
# # display
# print(data)

# first=data.loc['Avery Bradley']
# print(first)




# # importing pandas package
# import pandas as pd
  
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name")
  
# # retrieving rows by loc method
# rows = data.loc[["Avery Bradley", "R.J. Hunter"]]
  
# # checking data type of rows
# print(type(rows))
  
# # display
# print(rows)



# # importing pandas package
# import pandas as pd

# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Team")

# # retrieving rows by loc method
# rows = data.loc["Utah Jazz"]

# # checking data type of rows
# print(type(rows))

# # display
# print(rows)



# # importing pandas package
# import pandas as pd

# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name")

# # retrieving rows by loc method
# rows = data.loc["Avery Bradley":"Isaiah Thomas"]

# # checking data type of rows
# print(type(rows))

# # display
# print(rows)


# import pandas as pd

# data=pd.read_csv("nba.csv")
# row=data.loc[0:4,:]
# print(row)


# import pandas as pd

# df=pd.read_csv("nba.csv")
# print(df.columns)

# row=df.iloc[:,1:4]
# print(row)


# import pandas as pd

# data=pd.read_csv("nba.csv", index_col='Name')

# # print(df.head())

# print(data.loc['Avery Bradley':'Jonas Jerebko',:])


# import pandas as pd
# # data
# data = {
#    'Name': ['Hafeez', 'Srikanth', 'Rakesh'],
#    'Age': [19, 20, 19]
# }
# # creating a DataFrame with boolean index vector
# data_frame = pd.DataFrame(data, index = [True, False, True])
# print(data_frame)


# import pandas as pd

# data=pd.read_csv("nba.csv")

# team_grp=data.groupby("Team")

# # for g in team_grp:
# #     print(g)

# print(team_grp.groups)

# importing pandas module
# import pandas as pd 
# import numpy as np
   
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Anuj','Abhi', 'Jai', 'Princi', 
#                  'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
#         'Age':[27, 24,32, 22, 32, 
#                33, 36, 27, 32], 
#         'Address':['Nagpur', 'Kanpur','Patna', 'Allahabad', 'Kannuaj',
#                    'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
#         'Qualification':['Msc', 'MA','BE', 'MCA', 'Phd',
#                          'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1)
# gb=df.groupby('Name')

# sums=gb.aggregate(np.sum)
# print(sums)


# '''Using .concat() to concatenate two dataframes'''

# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# # Define a dictionary containing employee data 
# data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
#         'Age':[17, 14, 12, 52], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
# print(df)

 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
# print(df1)
 
 
# frame=[df,df1]

# res=pd.concat(frame)
# print(res)


# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
#         'Mobile No': [97, 91, 58, 76]} 
   
# # Define a dictionary containing employee data 
# data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
#         'Age':[22, 32, 12, 52], 
#         'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
#         'Salary':[1000, 2000, 3000, 4000]} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 

# # applying concat with axes join = 'inner'
# res2 = pd.concat([df, df1], axis=1,join='inner')
 
# print(res2)


# # importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# # Define a dictionary containing employee data 
# data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
#         'Age':[17, 14, 12, 52], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=[2,3, 6, 7])
 
# print(df, "\n\n", df1)

# res=df.append(df1, ignore_index=True)
# print(res)



# # importing pandas module
# import pandas as pd 
  
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
#         'Mobile No': [97, 91, 58, 76]} 
    
# # Define a dictionary containing employee data 
# data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
#         'Age':[22, 32, 12, 52], 
#         'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
#         'Salary':[1000, 2000, 3000, 4000]} 
  
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
  
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 

# res=pd.concat([df,df1],keys=['x','y'])
# print(res)


# importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# # creating a series
# s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')
 
# print(df, "\n\n", s1) 

# # combining series and dataframe
# res = pd.concat([df, s1], axis=1)
 
# print(res)

# '''Merging a dataframe with one unique key combination'''

# # importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32],} 
   
# # Define a dictionary containing employee data 
# data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1)
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2) 
  
 
# print(df, "\n\n", df1) 

# res=pd.merge(df,df1, on='key')


# '''Merging dataframe using multiple join keys.'''

# # importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K1', 'K0', 'K1'],
#          'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32],} 
   
# # Define a dictionary containing employee data 
# data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K0', 'K0', 'K0'],
#          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1)
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2) 
  
 
# print(df, "\n\n", df1)

# print()

# # merging dataframe using multiple keys
# res1 = pd.merge(df, df1, on=['key', 'key1'],how='inner')   #by default merge is inner join or "intersection"
 
# print(res1)

# '''Using Join'''

# # importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32]} 
   
# # Define a dictionary containing employee data 
# data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])


# print(df, "\n\n", df1)  

# res = df.join(df1)
 
# print(res)

# '''Creating a dates dataframe'''

# import pandas as pd
# import datetime
 
# # Create dates dataframe with frequency 
# data = pd.date_range('1/1/2011', periods = 10, freq ='H')
 
# print(data)

# x=datetime.datetime.now()
# print(x.month, x.year)


'''Working with text in pandas'''

# '''code 1'''

# import pandas as pd

# data = {'Name':['sushant','ajay', 'vijay', 'raj','vikram'],
#         'Age':[23,34,23,45,23]}

# df=pd.DataFrame(data)
# print(df)
# print()

# print("Converting to uppercase \n")

# df['Name']=df['Name'].str.upper()
# print(df)

'''Code 1'''

# # importing pandas module  
# import pandas as pd 
     
# # Define a dictionary containing employee data 
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data) 
    
# # dropping null value columns to avoid errors 
# df.dropna(inplace = True) 
    
# # new data frame with split value columns 
# df["Address"]= df["Address"].str.split("a",n=0,expand=False) 
   
# # df display  
# print(df)


# '''Code #2:'''

# # importing pandas module 
# import pandas as pd
 
# # reading csv file from url
# data = pd.read_csv("nba.csv")
 
# # overwriting column with replaced value of age
# data["Age"]= data["Age"].replace(25.0, "Twenty five")
 
# # creating a filter for age column 
# # where age = "Twenty five"
# # filter = data["Age"]=="Twenty five"
 
# # printing only filtered columns
# print(data.where(data['Age']=='Twenty five').dropna())


'''Code #1:'''

# # importing pandas module 
# import pandas as pd 
   
# # Define a dictionary containing employee data 
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data) 
 
# # making copy of address column 
# new = df["Address"].copy() 
   
# # concatenating address with name column 
# # overwriting name column 
# df["Name"]= df["Name"].str.cat(new, sep =", ") 
   
# # display 
# print(df)




