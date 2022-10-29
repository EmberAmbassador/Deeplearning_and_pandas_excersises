# Oschegow Nicolaj, Bruder Luca
import pandas as pd

df = pd.read_csv("ex27_data.csv",index_col=0,dtype={0:'Int64'})

# a)

titles = df.loc[:,'seen_ep1':'seen_ep6']
titles[titles.notnull()] = 'Yes'
titles[titles.isnull()] = 'No'
df.loc[:,'seen_ep1':'seen_ep6'] = titles

# b)

df.loc[:,'like_char1':'like_char14'] = df.loc[:,'like_char1':'like_char14'].replace(
    {'Very unfavorably':-2,'Somewhat unfavorably':-1,
     'Neither favorably nor unfavorably (neutral)':0, 
     'Somewhat favorably':1,'Very favorably':2})

# c)

#print(df[['fan_sw','fan_st']].loc[(df['fan_sw'] == 'No')&(df['fan_st'] == 'No')])

notFans = len(df.loc[(df['fan_sw'] == 'No')&(df['fan_st'] == 'No')].index) - 1
answersGiven = len(df.loc[(df['fan_sw'].notnull())&(df['fan_st'].notnull())].index) - 1
print("The number of respondants who are neither a fan of Star Wars nor Star Trek is: " + str(notFans))

# The answer has been rounded to 2 decimals to make it more readable.
print("About " + str(round(((notFans/answersGiven)*100), 2)) + "% of people who answeres both questions are fans of neither franchise.")

# d)

#print(df[['fan_sw', 'seen_ep1', 'seen_ep2', 'seen_ep3', 'seen_ep4', 'seen_ep5', 'seen_ep6']])
#print(df[['fan_sw', 'seen_ep1', 'seen_ep2', 'seen_ep3', 'seen_ep4', 'seen_ep5', 'seen_ep6']].loc[(df['fan_sw'] == 'Yes') & (
#    (df['seen_ep1'] == 'Yes') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
#    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'Yes') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
#    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'Yes') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
#    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'Yes') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
#    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'Yes') & (df['seen_ep6'] == 'No') |
#    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'Yes')
#    )])

# This is supposed to calculate the number of people who are fans of Star Wars (df['fan_sw'] == 'Yes') AND who have only seen on movie (df['seen_epX'] == 'Yes'). Since we have 6 conditions XOR seems
# to be out of the question. Thus the less elegent option of explicitly checking each individual condition was chosen.
exactlyOne = len(df.loc[(df['fan_sw'] == 'Yes') & (
    (df['seen_ep1'] == 'Yes') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'Yes') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'Yes') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'Yes') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'No') |
    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'Yes') & (df['seen_ep6'] == 'No') |
    (df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'No') & (df['seen_ep5'] == 'No') & (df['seen_ep6'] == 'Yes')
    )].index) - 1
fansSW = len(df.loc[df['fan_sw'] == 'Yes'].index) - 1
print("About " + str(round(((exactlyOne/fansSW)*100), 2)) + "% of the questioned people are fans of Star Wars and have only seen one of the movies.")

