import pandas as pd
import urllib3
import json

api_call = "https://public.tableau.com/api/gallery?page=0&count=25&galleryType=viz-of-the-day&language=en-us"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)

print(search_call)
df = pd.json_normalize(search_call['items'],max_level=0)
print(df.describe)
print(df.head)
print(df.columns)

Author = pd.json_normalize(df['authorName'],max_level=0)

print(Author)
