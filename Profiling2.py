import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

df = pd.read_csv('Data\\actorfilms.csv')

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("Actor_Report.html")

profset = profile.description_set
print(profset.keys())
attributes = profset["correlations"]
print(attributes.keys())
auto_correlations = attributes["auto"]
print(auto_correlations)

data = auto_correlations

data.to_csv('output\\AutocorrelationReport.csv', index = False)

print("Data Prepped")