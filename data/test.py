# import pandas as pd
#
# biopics = pd.read_csv("biopics.csv", encoding='latin-1')
#
# print(biopics.count())
# biopics = biopics.drop_duplicates()
#
# biopics = biopics.rename(columns={"box_office": "earnings"})
#
# biopics = biopics[~biopics['earnings'].isna()]
#
# biopics = biopics[biopics['year_release'] >= 1990]
#
# biopics['type_of_subject'] = biopics['type_of_subject'].astype("category")
#
# biopics['country'] = biopics['country'].astype("category")
# biopics['lead_actor_actress_know'] = biopics['lead_actor_actress'].apply(lambda x: False if pd.isna(x)  else True)
#
# biopics['earnings'] = biopics['earnings'].apply(lambda x:x/1000000)
# biopics = biopics[['title','year_release','earnings','country','type_of_subject','lead_actor_actress','lead_actor_actress_know']]
#
# biopics = biopics.sort_values(by='earnings',ascending=False)
#
# print(biopics.head())


import copy
# import numpy as np
#
# a = np.array([[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0]])
# print(a)
#
# m = a.shape[0]
# n = a.shape[1]

# for i in range(m):
#     for j in range(i,m):
#         tmp = a[j][i]
#         a[j][i] = a[i][j]
#         a[i][j] = tmp
#
# for j in range(m):
#     for i in range(0,m//2,1):
#         a[i][j],a[m-1-i][j] = a[m-1-i][j],a[i][j]

#
# b = copy.deepcopy(a)
#
# for i in range(m):
#     print(i,m-1-i)
#     b[m-1-i] = a[i]
#
# print(b)

