# import pandas as pd
import pandas as pd
 
# # list of strings
# lst = ['Geeks', 'For', 'Geeks', 'is', 
#             'portal', 'for', 'Geeks']
 
# # Calling DataFrame constructor on list
# df = pd.DataFrame(lst)
# print(df)

data = pd.read_csv("nba.csv")
print(data)

print('##########################')

five=data.head()



