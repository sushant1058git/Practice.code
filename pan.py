
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
import pandas as pd 
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj','Abhi', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24,32, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur','Patna', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA','BE', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
gb=df.groupby('Name')

sums=gb.aggregate(np.sum)
print(sums)

