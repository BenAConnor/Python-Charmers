import json
import pandas as pd
import urllib3

api_call = "https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)
print('search_call')

df = pd.json_normalize(search_call['results'],max_level=0)

print(df.describe)

workbook_meta = pd.json_normalize(df['workbookMeta'],max_level=0)
workbooks = pd.json_normalize(df['workbook'],max_level=0)

print(df.describe)

search_results = pd.concat([workbook_meta,workbooks],axis=1)

print(search_results)
print(df)
print(workbook_meta)
print(workbooks)

search_results.to_csv('output\\TableauPublicAPIResults.csv',index=False)


