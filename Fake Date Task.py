import pandas as pd
import numpy as np
from faker import Faker
import datetime

# set faker seed
Faker.seed(4321)
fake = Faker()

# define lists
employee_id = []
names = []
gender = []
address = []
job_title = []
start_date = []
date_of_birth = []
min_start_date = datetime.date(2013, 1, 4)
max_start_date = datetime.date(2023, 1, 4)
# loop to create 50 records
for a in range(50):
    # add number to list
    employee_id += [a]
    
    # define boolean True/False to determine gender
    boolean = fake.boolean()
    gender += [np.where(boolean,'Female','Male')]
    names += [np.where(boolean,fake.first_name_female()+" "+fake.last_name(),fake.first_name_male()+" "+fake.last_name())]

    address += [fake.address()]
    job_title += [fake.job()]
    start_date += [fake.date_between(min_start_date,max_start_date)]
    date_of_birth += [fake.date_of_birth(None,16,80)]

# add lists to dataframe, with column names
df = pd.DataFrame(
    {
        'employee_id': employee_id,
        'name': names,
        'gender': gender,
        'address': address,
        'start_date': start_date,
        'date_of_birth': date_of_birth
    }
    )

# write datasets to csv
df.to_csv('output\\fake_dataset.csv', index=False) 