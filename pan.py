
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



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Team")

# retrieving rows by loc method
rows = data.loc["Utah Jazz"]

# checking data type of rows
print(type(rows))

# display
print(rows)



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving rows by loc method
rows = data.loc["Avery Bradley":"Isaiah Thomas"]

# checking data type of rows
print(type(rows))

# display
print(rows)
