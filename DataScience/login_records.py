'''
**Question**:
For each user, find the date of their first 'Login' activity and the total 
number of unique activity types they have engaged in since that first login. 
Exclude users who have never logged in. Order the result by userID.

| userID | activityDate | activityType  |
|--------|--------------|---------------|
| 1      | 2023-01-01   | 'Login'       |
| 1      | 2023-01-02   | 'Comment'     |
| 2      | 2023-01-01   | 'Login'       |
| 2      | 2023-01-02   | 'Share'       |
| 3      | 2023-01-03   | 'Login'       |
| 3      | 2023-01-03   | 'Like'        |
| 3      | 2023-01-03   | 'Comment'     |
| 4      | 2023-01-04   | 'Login'       |
| 4      | 2023-01-05   | 'Login'       |
| 5      | 2023-01-06   | 'Comment'     |
| 5      | 2023-01-07   | 'Comment'     |

**Output**:
| userID | firstLoginDate | activityCount |
|--------|----------------|---------------|
| 1      | 2023-01-01     | 2             |
| 2      | 2023-01-01     | 2             |
| 3      | 2023-01-03     | 3             |
| 4      | 2023-01-04     | 1             |

---'''

import pandas as pd

def first_login(df):

    # filter out users who have never logged in
    df = df.loc[df.activityType.eq('Login').groupby(df.userID).transform('any')]

    return df.groupby('userID').agg({'activityDate': 'min', 'activityType': 'nunique'}).reset_index().rename(columns={'activityDate': 'firstLoginDate', 'activityType': 'activityCount'})

df = pd.DataFrame({'userID': [1,1,2,2,3,3,3,4,4,5,5], 
                   'activityDate': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07'], 
                   'activityType': ['Login', 'Comment', 'Login', 'Share', 'Login', 'Like', 'Comment', 'Login', 'Login','Comment','Comment']})

print(first_login(df))